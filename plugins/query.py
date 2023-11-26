import os, time, asyncio,sys
import humanize
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import Compress_Stats, Skip, CompressVideo
from helper.database import db
from script import Txt

@Client.on_callback_query()
async def Cb_Handle(bot:Client, query:CallbackQuery):
    data = query.data

    if data == 'help':

        btn = [
            [InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='home')]
        ]

        await query.message.edit(text=Txt.HELP_MSG, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
        

    if data == 'home':
        btn = [
            [InlineKeyboardButton(text='❗ Hᴇʟᴘ', callback_data='help'), InlineKeyboardButton(text='🌨️ Aʙᴏᴜᴛ', callback_data='about')],
            [InlineKeyboardButton(text='📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/AIORFT'), InlineKeyboardButton(text='💻 Dᴇᴠᴇʟᴏᴘᴇʀ', callback_data='https://t.me/Snowball_Official')]
        ]
        await query.message.edit(text=Txt.PRIVATE_START_MSG.format(query.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))


    if data == 'stats':
        try:
            downpath = f"Downloads/{query.from_user.id}/{os.listdir(f'Downloads/{query.from_user.id}')[0]}"
            encodepath = f"Encode/{query.from_user.id}/{os.listdir(f'Encode/{query.from_user.id}')[0]}"


            await Compress_Stats(e=query, inp=downpath, outp=encodepath, userid=query.from_user.id)
            
        except Exception as e:
            print(e)
    
    elif data == 'Skip':
        try:
            await Skip(query, query.from_user.id)
        except Exception as e:
            print(e)
        
    elif data == 'compress':
        BTNS = [
        [InlineKeyboardButton(text='𝖵𝖠𝖱𝖨𝖠𝖡𝖫𝖤 1', callback_data='basiccomp')],
        [InlineKeyboardButton(text='𝖵𝖠𝖱𝖨𝖠𝖡𝖫𝖤 2', callback_data='highlycomp')],
        [InlineKeyboardButton(text='𝖢𝖴𝖲𝖳𝖮𝖬', callback_data='customcomp')],
        [InlineKeyboardButton(text='⟸ Bᴀᴄᴋ', callback_data='option')]
    ]
        await query.message.edit(text='**Change your metadata below 👇 **', reply_markup=InlineKeyboardMarkup(BTNS))
        
    
    elif data == 'option':
        file = getattr(query.message.reply_to_message, query.message.reply_to_message.media.value)
        
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{file.file_name}`\n\n**File Size** :- `{humanize.naturalsize(file.file_size)}`"""
        buttons = [[InlineKeyboardButton("", callback_data="rename")],
                    [InlineKeyboardButton("📝 𝖢𝖧𝖠𝖭𝖦𝖤 𝖬𝖤𝖳𝖠𝖣𝖠𝖳𝖠 📝", callback_data="compress")]]
        
        await query.message.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        
    elif data == 'basiccomp':
        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-map 0 -c:s copy -c:a copy -c:v copy -metadata title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata author=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:s title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:a title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:v title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺"
            await CompressVideo(bot=bot, query=query, ffmpegcode="-map 0 -c:s copy -c:a copy -c:v copy -metadata title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata author=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:s title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:a title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺 -metadata:s:v title=@𝖠𝗇𝗂𝗆𝖾_𝖲𝗎𝗉𝖾𝗋𝗇𝗈𝗏𝖺", c_thumb=c_thumb)
            
        except Exception as e:
            print(e)
    
    elif data == 'highlycomp':
        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-map 0 -c:s copy -c:a copy -c:v copy -metadata title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata author=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:s title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:a title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:v title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑"
            await CompressVideo(bot=bot, query=query, ffmpegcode="-map 0 -c:s copy -c:a copy -c:v copy -metadata title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata author=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:s title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:a title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑 -metadata:s:v title=@𝖲𝖾𝗋𝗂𝖾𝗌_𝖬𝗈𝗏𝗂𝖾𝗌_𝖯𝖺𝗋𝖺𝖽𝗈𝗑", c_thumb=c_thumb)
            
        except Exception as e:
            print(e)
    
    elif data == 'customcomp':

        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg_code = await db.get_ffmpegcode(query.from_user.id)

            if ffmpeg_code:
                await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg_code, c_thumb=c_thumb)
            
            else:
                BUTT = [
                    [InlineKeyboardButton(text='𝖲𝖾𝗍 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝖵𝖺𝗋𝗂𝖺𝖻𝗅𝖾', callback_data='setffmpeg')],
                    [InlineKeyboardButton(text='⟸ Bᴀᴄᴋ', callback_data='compress')]
                ]
                await query.message.edit(text="You Don't Have Any Custom Metadata Variables. 🛃", reply_markup=InlineKeyboardMarkup(BUTT))
        except Exception as e:
            print(e)
        
    elif data == 'setffmpeg':
        ffmpeg_code = await bot.ask(text=Txt.SEND_FFMPEG_CODE , chat_id= query.from_user.id, filters = filters.text, timeout=60, disable_web_page_preview=True)
        SnowDev = await query.message.reply_text(text="**Setting Your FFMPEG CODE**\n\nPlease Wait...")
        await db.set_ffmpegcode(query.from_user.id, ffmpeg_code.text)
        await SnowDev.edit("✅️ __**𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝖵𝖺𝗋𝗂𝖺𝖻𝗅𝖾𝗌 𝖲𝖾𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**__")

    elif data == 'about':
        BUTN = [
            [InlineKeyboardButton(text='⟸ Bᴀᴄᴋ', callback_data='home')]
        ]
        botuser = await bot.get_me()
        await query.message.edit(Txt.ABOUT_TXT.format(botuser.username), reply_markup=InlineKeyboardMarkup(BUTN), disable_web_page_preview=True)


    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
