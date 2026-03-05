from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "YOUR_BOT_TOKEN"
BOT_OWNER_ID = 8028749711  # 👈 Apna Telegram ID

# Links
OWNER_LINK = "https://t.me/CarelessxOwner"
SUPPORT_LINK = "https://t.me/CarelessxWorld"
UPDATE_LINK = "https://t.me/ll_CarelessxCoder_ll"

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

sessions = {}  # user_id -> session data

# =========================
# MESSAGES AS VARIABLES
# =========================
WELCOME_MSG = f"""<b>Welcome to the Multi-Menu Post Bot!</b>

Use buttons below to navigate. Add me to your group or channel and generate posts easily.
"""

HELP_MSG = f"""<b>Help Section:</b>

Here you can see instructions for using the bot.
1️⃣ Add bot to your channel/group
2️⃣ Make bot admin
3️⃣ Use 'Generate Post' to create posts
"""

ABOUT_MSG = f"""<b>About Section:</b>

This bot is created for multi-menu post generation demo.
You can customize this text anytime.
"""

CONTROL_PANEL_MSG = f"""<b>╔═══❖ CONTROL PANEL ❖═══╗</b>

Choose an action below. Add buttons, preview your post, or publish it.
"""

# =========================
# INLINE KEYBOARDS
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

def help_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔙 Back", callback_data="back_welcome"))
    return keyboard

def about_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("👑 Owner", url=OWNER_LINK))
    keyboard.add(
        InlineKeyboardButton("📢 Updates", url=UPDATE_LINK),
        InlineKeyboardButton("🛠 Support", url=SUPPORT_LINK)
    )
    return keyboard

def control_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ Add Button", callback_data="add_btn"),
        InlineKeyboardButton("👁 Preview", callback_data="preview")
    )
    keyboard.add(InlineKeyboardButton("🚀 Publish", callback_data="publish"))
    return keyboard

# =========================
# START COMMAND
# =========================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(WELCOME_MSG, reply_markup=await welcome_keyboard())

# =========================
# CALLBACK HANDLER
# =========================
@dp.callback_query_handler(lambda c: True)
async def callbacks(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data

    # ---------- MENU NAVIGATION ----------
    if data == "help":
        await callback.message.edit_text(HELP_MSG, reply_markup=help_keyboard())
    elif data == "about":
        await callback.message.edit_text(ABOUT_MSG, reply_markup=about_keyboard())
    elif data == "back_welcome":
        await callback.message.edit_text(WELCOME_MSG, reply_markup=await welcome_keyboard())

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

    await callback.answer()

# =========================
# MESSAGE HANDLER
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

    # ---------- STEP 4: ADD BUTTONS ----------
    elif step == "button_text":
        session["button_text"] = message.text
        session["step"] = "button_url"
        await message.reply(
            "<b>Send Button URL or callback data</b>:\n"
            "If external link, start with https://\n"
            "If bot action, send callback_data like 'generate_post'"
        )

    elif step == "button_url":
        btn_text = session.pop("button_text")
        btn_input = message.text.strip()

        if btn_input.startswith("http://") or btn_input.startswith("https://"):
            new_button = InlineKeyboardButton(btn_text, url=btn_input)
        else:
            new_button = InlineKeyboardButton(btn_text, callback_data=btn_input)

        await message.reply(
            "Type 'single' for new row, 'same' for same row as previous button."
        )
        session["new_button"] = new_button
        session["step"] = "button_line_choice"

    elif step == "button_line_choice":
        new_button = session.pop("new_button")
        placement = message.text.strip().lower()

        if placement == "same" and session["rows"]:
            session["rows"][-1].append(new_button)
        else:
            session["rows"].append([new_button])

        session["step"] = "control"
        await send_control_panel(message, added=True)

# =========================
# CONTROL PANEL FUNCTION
# =========================
async def send_control_panel(message, added=False):
    user_id = message.from_user.id
    keyboard = control_keyboard()
    text = CONTROL_PANEL_MSG
    if added:
        text += "\n✅ Button Added!"
    await message.reply(text, reply_markup=keyboard)

# =========================
# START BOT
# =========================
if __name__ == "__main__":
    executor.start_polling(dp)
