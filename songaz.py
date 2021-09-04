#Kirito Z E N
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import youtube_dl
from youtube_search import YoutubeSearch
import requests

from pyrogram import Client, filters
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton
import time


import os
from apim import Config

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")


TG = Client(
    'AsunaMusic',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

async def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@TG.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Salam! {message.from_user.mention}👤\nMən sənin asanlıqla istədiyin mahnını yükləməyə kömək edəcək botam✅\nBotda reklam vermək istəsən sahibimlə əlaqə saxla.\n\nNümunə:\n/musiqi Əlimdə Roza 🎵!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅Qrupa əlavə et", url="https://t.me/song_azbot?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "🛎Rəsmi Qrupumuz", url="https://t.me/songazerbaycan"),
                    InlineKeyboardButton(
                        "☑️ Rəsmi kanal", url="https://t.me/elisbots")     
                ],[ 
                    InlineKeyboardButton(
                        "🇦🇿PlayList", url="t.me/zenmusiqi"
                        )
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

    
@TG.on_message(filters.command("musiqi") & filters.private & ~filters.channel)
def song(client, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Axtarılır...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('Heçnə tapılmadı! Düzgün yazın')
            return
    except Exception as e:
        m.edit(
            "✖️Xahiş nümunədə olduğu kimi qeyd edin`\n/musiqi Miro Sevgin batsın`"
        )
        print(str(e))
        return
    m.edit(f"`{title}` yüklənir✅")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🇦🇿**{title}**\n\n      🎶Xoş Dinləmələr \n\n✅Yüklədi: [Song🇦🇿](https://t.me/song_azbot) \n↗️PlayList: [Toxun🎵](https://t.me/zenmusiqi)' 
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
            quote=False,

        message.reply_audio(audio_file, caption=rep, parse_mode='md', title=title, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌Xəta\n\n Xətanı bildirmək üçün @abbasov1o ❤️')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


TG.run()
