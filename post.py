from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "YOUR_BOT_TOKEN"
BOT_OWNER_ID = 123456789  # 👈 Apna Telegram ID

# Links
OWNER_LINK = "https://t.me/CarelessxOwner"
SUPPORT_LINK = "https://t.me/CarelessxWorld"
UPDATE_LINK = "https://t.me/ll_CarelessxCoder_ll"

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

sessions = {}  # user_id -> session data

# =========================
# WELCOME MENU
# =========================
async def welcome_keyboard():
    me = await bot.get_me()
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ Add Me in Group", url=f"https://t.me/{me.username}?startgroup=true"),
        InlineKeyboardButton("➕ Add Me in Channel", url=f"https://t.me/{me.username}?startchannel=true")
    )
    keyboard.add(InlineKeyboardButton("📝 Generate Post", callback_data="generate_post"))
    keyboard.add(
        InlineKeyboardButton("❓ Help", callback_data="help"),
        InlineKeyboardButton("ℹ️ About", callback_data="about")
    )
    return keyboard

# =========================
# HELP MENU
# =========================
def help_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔙 Back", callback_data="back_welcome"))
    return keyboard

# =========================
# ABOUT MENU
# =========================
def about_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("👑 Owner", url=OWNER_LINK))
    keyboard.add(
        InlineKeyboardButton("📢 Updates", url=UPDATE_LINK),
        InlineKeyboardButton("🛠 Support", url=SUPPORT_LINK)
    )
    return keyboard

# =========================
# Start Command
# =========================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text = "<b>Welcome to the Multi-Menu Post Bot!</b>\n\nUse buttons below to navigate."
    await message.answer(text, reply_markup=await welcome_keyboard())

# =========================
# CALLBACK HANDLER
# =========================
@dp.callback_query_handler(lambda c: True)
async def callbacks(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data

    # ---------- MENU NAVIGATION ----------
    if data == "help":
        await callback.message.edit_text(
            "<b>Help Section:</b>\n\nHere you can see instructions for using the bot.",
            reply_markup=help_keyboard()
        )
    elif data == "about":
        await callback.message.edit_text(
            "<b>About Section:</b>\n\nThis bot is created for multi-menu demo.\nYou can customize this text.",
            reply_markup=about_keyboard()
        )
    elif data == "back_welcome":
        await callback.message.edit_text(
            "<b>Welcome to the Multi-Menu Post Bot!</b>\n\nUse buttons below to navigate.",
            reply_markup=await welcome_keyboard()
        )

    # ---------- GENERATE POST ----------
    elif data == "generate_post":
        sessions[user_id] = {"step": "channel", "rows": []}
        await bot.send_message(user_id, "<b>Send your Channel or Group username:</b>\nExample: <code>@mychannel</code>")

    # ---------- ADD BUTTON ----------
    elif data == "add_btn" and user_id in sessions:
        sessions[user_id]["step"] = "button_text"
        await bot.send_message(user_id, "<b>Send Button Text</b>")

    # ---------- PREVIEW ----------
    elif data == "preview" and user_id in sessions:
        session = sessions[user_id]
        markup = InlineKeyboardMarkup()
        for row in session["rows"]:
            markup.row(*row)
        if session.get("media"):
            if session["media_type"]=="photo":
                await bot.send_photo(user_id, session["media"], caption=session["text"], reply_markup=markup)
            elif session["media_type"]=="video":
                await bot.send_video(user_id, session["media"], caption=session["text"], reply_markup=markup)
        else:
            await bot.send_message(user_id, session["text"], reply_markup=markup)

    # ---------- PUBLISH ----------
    elif data == "publish" and user_id in sessions:
        session = sessions[user_id]
        markup = InlineKeyboardMarkup()
        for row in session["rows"]:
            markup.row(*row)

        try:
            # Check if user is admin in channel/group
            member = await bot.get_chat_member(session["channel"], user_id)
            if member.status not in ["administrator", "creator"] and user_id != BOT_OWNER_ID:
                await bot.send_message(user_id, "❌ You are not admin of this channel!")
                return

            if session.get("media"):
                if session["media_type"]=="photo":
                    await bot.send_photo(session["channel"], session["media"], caption=session["text"], reply_markup=markup)
                elif session["media_type"]=="video":
                    await bot.send_video(session["channel"], session["media"], caption=session["text"], reply_markup=markup)
            else:
                await bot.send_message(session["channel"], session["text"], reply_markup=markup)

            await bot.send_message(user_id, "🎉 Post Published Successfully!")
        except Exception as e:
            await bot.send_message(user_id, f"❌ Error:\n<code>{e}</code>")

        sessions.pop(user_id, None)

    await callback.answer()  # remove loading icon

# =========================
# MESSAGE HANDLER FOR POST CREATION
# =========================
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in sessions:
        return

    session = sessions[user_id]
    step = session["step"]

    # ---------- STEP 1: CHANNEL ----------
    if step == "channel":
        session["channel"] = message.text
        session["step"] = "content"
        await message.reply("Send post text (you can use <b>HTML</b> formatting).")

    # ---------- STEP 2: CONTENT ----------
    elif step == "content":
        session["text"] = message.text
        session["media"] = None
        session["media_type"] = None
        session["step"] = "media"
        await message.reply("Send photo/video OR type /skip to continue without media.")

    # ---------- STEP 3: MEDIA ----------
    elif step == "media":
        if message.text == "/skip":
            session["step"] = "control"
            await send_control_panel(message)
            return

        if message.photo:
            session["media"] = message.photo[-1].file_id
            session["media_type"] = "photo"
        elif message.video:
            session["media"] = message.video.file_id
            session["media_type"] = "video"
        else:
            await message.reply("Send valid photo/video OR type /skip.")
            return

        session["step"] = "control"
        await send_control_panel(message)

# =========================
# CONTROL PANEL
# =========================
async def send_control_panel(message, added=False):
    user_id = message.from_user.id
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ Add Button", callback_data="add_btn"),
        InlineKeyboardButton("👁 Preview", callback_data="preview")
    )
    keyboard.add(InlineKeyboardButton("🚀 Publish", callback_data="publish"))

    text = "<b>╔═══❖ CONTROL PANEL ❖═══╗</b>\n"
    if added:
        text += "✅ Button Added!\n"
    text += "Choose an action:"
    await message.reply(text, reply_markup=keyboard)

# =========================
# Start Polling
# =========================
if __name__ == "__main__":
    executor.start_polling(dp)
