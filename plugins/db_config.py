from pyrogram import Client, filters, enums
from helper.database import db
from helper.utils import CANT_CONFIG_GROUP_MSG
from script import Txt
from asyncio.exceptions import TimeoutError


@Client.on_message((filters.group | filters.private) & filters.command('set_caption'))
async def add_caption(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Cᴀᴩᴛɪᴏɴ__\n\nExᴀᴍᴩʟᴇ:- `/set_caption {filename}\n\n💾 Sɪᴢᴇ: {filesize}\n\n⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`**")

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ Cᴀᴩᴛɪᴏɴ Sᴀᴠᴇᴅ**__")


@Client.on_message((filters.group | filters.private) & filters.command('del_caption'))
async def delete_caption(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return


    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    caption = await db.get_caption(message.from_user.id)
    if not caption:
        return await SnowDev.edit("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**__")
    await db.set_caption(message.from_user.id, caption=None)
    await SnowDev.edit("__**❌️ Cᴀᴩᴛɪᴏɴ Dᴇʟᴇᴛᴇᴅ**__")


@Client.on_message((filters.group | filters.private) & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    caption = await db.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"**Yᴏᴜ'ʀᴇ Cᴀᴩᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
        await message.reply_text("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**__")


@Client.on_message((filters.group | filters.private) & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await SnowDev.delete()
        await client.send_photo(chat_id=message.chat.id, photo=thumb, reply_to_message_id=message.id)
    else:
        await SnowDev.edit("😔 __**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Tʜᴜᴍʙɴᴀɪʟ**__")


@Client.on_message((filters.group | filters.private) & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    await db.set_thumbnail(message.from_user.id, thumbnail=None)
    await SnowDev.edit("❌️ __**Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ**__")


@Client.on_message((filters.group | filters.private) & filters.photo)
async def addthumbs(client, message):
    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    await db.set_thumbnail(message.from_user.id, message.photo.file_id)
    await SnowDev.edit("✅️ __**Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ**__")
    

@Client.on_message((filters.group | filters.private) & filters.command(['set_metadata', 'setmetadata']))
async def set_metadata(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return
    try:
        ffmpeg = await client.ask(text=Txt.SEND_FFMPEG_CODE, chat_id=message.chat.id,
                            user_id=message.from_user.id, filters=filters.text, timeout=30, disable_web_page_preview=True)
    except TimeoutError:
        await bot.send_message(message.from_user.id, "Error!!\n\nRequest timed out.\nRestart by using /set_ffmpeg")
        return
        
    await db.set_metadata(message.from_user.id, ffmpeg.text)
    await message.reply_text("😔 __**Pʟᴇᴀsᴇ Bᴜʏ Pʀᴏ Pʟᴀɴ Tᴏ Aᴄᴄᴇss Tʜɪs Fᴇᴀᴛᴜʀᴇ**__", reply_to_message_id=message.id)


@Client.on_message((filters.group | filters.private) & filters.command(['see_metadata', 'seemetadata']))
async def see_metadata(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)

    ffmpeg = await db.get_metadata(message.from_user.id)
    
    if ffmpeg:
        await SnowDev.edit(f"😔 <b> Pʟᴇᴀsᴇ Bᴜʏ Pʀᴏ Pʟᴀɴ Tᴏ Aᴄᴄᴇss Tʜɪs Fᴇᴀᴛᴜʀᴇ")
    else:
        await SnowDev.edit(f"😔 __**Pʟᴇᴀsᴇ Bᴜʏ Pʀᴏ Pʟᴀɴ Tᴏ Aᴄᴄᴇss Tʜɪs Fᴇᴀᴛᴜʀᴇ**__")


@Client.on_message((filters.group | filters.private) & filters.command(['del_metadata', 'delmetadata']))
async def del_metadata(client, message):

    if message.chat.type == enums.ChatType.SUPERGROUP:
        await CANT_CONFIG_GROUP_MSG(client, message)
        return

    SnowDev = await message.reply_text(text="**Please Wait...**", reply_to_message_id=message.id)
    await db.set_metadata(message.from_user.id, None)
    await SnowDev.edit("😔 __**Pʟᴇᴀsᴇ Bᴜʏ Pʀᴏ Pʟᴀɴ Tᴏ Aᴄᴄᴇss Tʜɪs Fᴇᴀᴛᴜʀᴇ**__")
