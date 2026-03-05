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
WELCOME_MSG = f"""<b>👋 ʜᴇʟʟᴏ  !</b>
<b>❍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ˹𝐏ᴏsᴛ ꭙ 𝐌ᴀᴋᴇʀ˼. 🥳</b>
<b>✦━━━━━━━━━━━━━━━━━━━━━✦</b>
<b>🛠 ⚠️ ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛɪᴄᴇ :</b>
<b>➜ Mᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ.</b>
<b>➜ ʙᴏᴛ ʜᴀᴠᴇ sᴏᴍᴇ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴘᴇʀᴍɪssɪᴏɴ ʟɪᴋᴇ  </b>
❍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ 
❍ sᴇɴᴅ ᴍᴇssᴀɢᴇs 
❍ ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs
<b>✦━━━━━━━━━━━━━━━━━━━━━✦</b>
<b>➤ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/CarelessxOwner">˹ᴍɪsᴛᴇʀ ꭙ sᴛᴀʀᴋ˼</a></b>
<b>➤ ᴍᴏʀᴇ ʙᴏᴛs : <a href="https://t.me/StarkxNetwrk">˹sᴛᴀʀᴋ ꭙ ɴᴇᴛᴡᴏʀᴋ˼</a></b>
<b>➤ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href="https://t.me/ll_CarelessxCoder_ll">˹ᴄᴀʀᴇʟᴇss ꭙ ᴄᴏᴅᴇʀ˼</a></b>
<b>╰─━━━  ✦ ❀ ✦ ❖ ✦ ❀ ✦   ━━━─</b>
"""

HELP_MSG = f"""╔════════════════════╗
       ✦ ᴘᴏꜱᴛ ᴄʀᴇᴀᴛɪᴏη ɢᴜɪᴅᴇ ✦
╚════════════════════╝

<b>➻ ᴇηꜱᴜʀᴇ ʙᴏᴛ ʜᴀꜱ ᴀᴅᴍɪη ʀɪɢʜᴛꜱ ʙᴇꜰᴏʀᴇ ᴄʀᴇᴀᴛɪηɢ ᴘᴏꜱᴛꜱ</b>
   ➤ Oηʟʏ ᴀꜰᴛᴇʀ ꜰᴜʟʟ ᴀᴅᴍɪη ʀɪɢʜᴛꜱ, ʙᴏᴛ ᴄᴀη ᴄʀᴇᴀᴛᴇ ᴘᴏꜱᴛꜱ  
   ➤ Mɪssɪηɢ ᴘᴇʀᴍɪꜱꜱɪᴏηꜱ ᴄᴀᴜꜱᴇ ᴇʀʀᴏʀꜱ ᴏʀ ꜰᴀɪʟᴜʀᴇ
<b>✦━━━━━━━━━━━━━━━━━━━━━✦</b>
<b>➻ ꜱᴛᴀʀᴛ ᴄʀᴇᴀᴛɪηɢ ᴘᴏꜱᴛꜱ ᴡɪᴛʜ “ɢᴇηᴇʀᴀᴛᴇ ᴘᴏꜱᴛ”</b>
   ➤ ᴀꜰᴛᴇʀ ᴀᴅᴅɪηɢ ᴀηᴅ ᴘʀᴏᴍᴏᴛɪηɢ ʙᴏᴛ, ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏη  
   ➤ Sᴇηᴅ ᴘᴏꜱᴛ ᴛᴇxᴛ, ᴀᴛᴛᴀᴄʜ ᴘʜᴏᴛᴏ/ᴠɪᴅᴇᴏ & ʙᴜɪʟᴅ ᴄᴏɴᴛᴇηᴛ
<b>✦━━━━━━━━━━━━━━━━━━━━━✦</b>
<b>➻ ᴀᴅᴅ ɪηʟɪηᴇ ʙᴜᴛᴛᴏηꜱ ꜰᴏʀ ʏᴏᴜʀ ᴘᴏꜱᴛꜱ </b>
   ➤ ᴀᴅᴅ ᴍᴜʟᴛɪᴘʟᴇ ʙᴜᴛᴛᴏηꜱ  
   ➤ Tᴡᴏ ᴘʟᴀᴄᴇᴍᴇηᴛ ᴏᴘᴛɪᴏηꜱ:  
     ❍ ꜱɪηɢʟᴇ ʟɪηᴇ → ᴇᴀᴄʜ ʙᴜᴛᴛᴏη ᴏɴ ɪᴛꜱ ᴏᴡη ʀᴏᴡ  
     ❍ ꜱᴀᴍᴇ ʟɪηᴇ → ᴍᴜʟᴛɪᴘʟᴇ ʙᴜᴛᴛᴏηꜱ ɪη ᴏɴᴇ ʀᴏᴡ
<b>✦━━━━━━━━━━━━━━━━━━━━━✦</b>
<b>➻ ᴘʀᴇᴠɪᴇᴡ ʏᴏᴜʀ ᴘᴏꜱᴛ ʙᴇꜰᴏʀᴇ ᴘᴜʙʟɪꜱʜɪηɢ </b>
   ➤ ᴜꜱᴇ ᴘʀᴇᴠɪᴇᴡ ᴏᴘᴛɪᴏη ᴛᴏ ᴄʜᴇᴄᴋ ꜰᴏʀᴍᴀᴛᴛɪηɢ, ᴍᴇᴅɪᴀ & ʙᴜᴛᴛᴏηꜱ  
   ➤ Sᴀᴛɪꜱꜰɪᴇᴅ? ᴄʟɪᴄᴋ ᴘᴜʙʟɪꜱʜ ᴛᴏ ᴅᴇʟɪᴠᴇʀ.
"""

ABOUT_MSG = f"""<b>╭─━━━ ✦ ᴀʙᴏᴜᴛ ʙᴏᴛ ✦ ━━━─╮</b>
<b>│</b>
<b>│ 🤖 ɴᴀᴍᴇ : ᴍɪsᴛᴇʀ sᴛᴀʀᴋ</b>
<b>│ 👑 ᴏᴡɴᴇʀ : <a href="https://t.me/CarelessxOwner">˹ᴍɪsᴛᴇʀ ꭙ sᴛᴀʀᴋ˼</a></b>
<b>│ 📢 ᴜᴘᴅᴀᴛᴇs : <a href="https://t.me/ll_CarelessxCoder_ll">˹ᴄᴀʀᴇʟᴇss ꭙ ᴄᴏᴅᴇʀ˼</a></b>
<b>│ 🚀 ᴠᴇʀsɪᴏɴ : v2.6</b>
<b>│ 🐍 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>
<b>│ 📚 ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
<b>│ 📡 ʜᴏsᴛᴇᴅ ᴏɴ : ᴠᴘs</b>
<b>│</b>
<b>╰━ ✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href="https://t.me/ll_CarelessxCoder_ll">˹ᴄᴀʀᴇʟᴇss ꭙ ᴄᴏᴅᴇʀ˼</a></b>
"""

CONTROL_PANEL_MSG = f"""<b>╔══❖ CONTROL PANEL ❖══╗</b>

<b>➤ 𝗔𝗱𝗱 𝗕𝘂𝘁𝘁𝗼𝗻</b> 
 <b>➻ ᴜꜱᴇ ᴛʜɪꜱ ᴛᴏ ᴀᴅᴅ ɪηʟɪηᴇ ʙᴜᴛᴛᴏηꜱ ᴛᴏ ʏᴏᴜʀ ᴘᴏꜱᴛ</b>
<b>➻ Sᴇηᴅ ᴛʜᴇ ʙᴜᴛᴛᴏη ᴛᴇxᴛ ꜰɪʀꜱᴛ, ᴛʜᴇɴ ᴛʜᴇ URL ᴏʀ ᴄᴀʟʟʙᴀᴄᴋ ᴅᴀᴛᴀ</b>
<b>➻ ʏᴏᴜ ᴄᴀη ᴄʜᴏᴏꜱᴇ ᴛᴏ ᴘʟᴀᴄᴇ ᴛʜᴇ ʙᴜᴛᴛᴏη ɪη ᴀ ɴᴇᴡ ʀᴏᴡ ᴏʀ ᴛʜᴇ ꜱᴀᴍᴇ ʀᴏᴡ ᴀꜱ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʙᴜᴛᴛᴏη</b>

<b>➤ 𝗣𝗿𝗲𝘃𝗶𝗲𝘄</b>
<b>➻ ᴄʜᴇᴄᴋ ʜᴏᴡ ʏᴏᴜʀ ᴘᴏꜱᴛ ᴡɪʟʟ ʟᴏᴏᴋ ʙᴇꜰᴏʀᴇ ᴘᴜʙʟɪꜱʜɪηɢ  
Pʀᴇᴠɪᴇᴡ ꜱʜᴏᴡꜱ ᴛʜᴇ ᴛᴇxᴛ, ᴍᴇᴅɪᴀ & ʙᴜᴛᴛᴏηꜱ ᴛᴏɢᴇᴛʜᴇʀ ꜱᴏ ʏᴏᴜ ᴄᴀη ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴇᴠᴇʀʏᴛʜɪηɢ ɪꜱ ᴄᴏʀʀᴇᴄᴛ. </b>

<b>➤ 𝗣𝘂𝗯𝗹𝗶𝘀𝗵</b> 
<b>➻ ꜱᴇηᴅ ʏᴏᴜʀ ᴘᴏꜱᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀηηᴇʟ ᴏʀ ɢʀᴏᴜᴘ</b> 
<b>➻ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴠᴇʀɪꜰʏ ᴀᴅᴍɪη ʀɪɢʜᴛꜱ ʙᴇꜰᴏʀᴇ ᴘᴜʙʟɪꜱʜɪηɢ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴇʀʀᴏʀꜱ. </b>
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
# START COMMAND WITH SPOILER PHOTO
# =========================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    me = await bot.get_me()
    keyboard = await welcome_keyboard()
    photo_url = "https://files.catbox.moe/dgelfj.jpg"
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=WELCOME_MSG,
        parse_mode="HTML",
        reply_markup=keyboard,
        has_spoiler=True  # <-- spoiler photo
    )

# =========================
# CALLBACK HANDLER
# =========================
@dp.callback_query_handler(lambda c: True)
async def callbacks(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data

    if data == "help":
        await callback.message.edit_text(HELP_MSG, reply_markup=help_keyboard())
    elif data == "about":
        await callback.message.edit_text(ABOUT_MSG, reply_markup=about_keyboard())
    elif data == "back_welcome":
        await callback.message.delete()
        await start(callback.message)  # resend welcome with spoiler photo

    elif data == "generate_post":
        sessions[user_id] = {"step": "channel", "rows": []}
        await bot.send_message(user_id, "<b>Send your Channel or Group username:</b>\nExample: <code>@mychannel</code>")

    elif data == "add_btn" and user_id in sessions:
        sessions[user_id]["step"] = "button_text"
        await bot.send_message(user_id, "<b>Send Button Text</b>")

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

    # STEP 1: CHANNEL
    if step == "channel":
        session["channel"] = message.text
        session["step"] = "content"
        await message.reply("Send post text (you can use <b>HTML</b> formatting).")

    # STEP 2: CONTENT
    elif step == "content":
        session["text"] = message.text
        session["media"] = None
        session["media_type"] = None
        session["step"] = "media"
        await message.reply("Send photo/video OR type /skip to continue without media.")

    # STEP 3: MEDIA
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

    # STEP 4: ADD BUTTON
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
# RUN BOT
# =========================
if __name__ == "__main__":
    executor.start_polling(dp)
