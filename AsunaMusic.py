#Kirito Z E N
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import youtube_dl
from youtube_search import YoutubeSearch
import requests

from pyrogram import Client, filters
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton
import time

import os
from config import Config

TG = Client(
    'AsunaMusic',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

def ydl():
	BUTTON=[[InlineKeyboardButton(text="🔊 Rəsmi Kanal", url="https://t.me/zenmusiqi")]]
	BUTTON+=[[InlineKeyboardButton(text="➕ Grupa Əlavə Et ➕", url=f"https://t.me/song_azbot?startgroup=true")]]
	return InlineKeyboardMarkup(BUTTON)
## Extra Fns -------------------------------

# Convert hh:mm:ss to seconds
async def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands --------------------------------
@TG.on_message(filters.command("start")&filters.private)
def start(client, message):
    Asuna = f'👋Salam {message.from_user.mention}\nMusiqi yükləmə botuyam💿\n\nNümunə:`/musiqi Miro Sevgin batsın`'
    message.reply_text(
        text=Asuna, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('PlayList🇦🇿', url='https://t.me/zenmusiqi'),
                    InlineKeyboardButton('Qrupa əlavə et➕', url='https://t.me/song_azbot?startgroup=true')
                ]
            ]
        )
    )

@TG.on_message(filters.command("start")&filters.group)
def start(client, message):
    Asuna = f'👋Salam {message.from_user.mention}\nMusiqi yükləmə botuyam💿\n\nNümunə:`/musiqi Miro Sevgin batsın`'
    message.reply_text(
        text=Asuna, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('PlayList🇦🇿', url='https://t.me/zenmusiqi'),
                    InlineKeyboardButton('Qrupa əlavə et➕', url='https://t.me/song_azbot?startgroup=true')
                ]
            ]
        )
    )

@TG.on_message(filters.command("musiqi")&filters.private)
def a(client, message):
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
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

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
    m.edit(f"`{title[:35]}` yüklənir✅")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🇦🇿**{title[:35]}** | @song_azbot' 
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
            quote=False,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('PlayList🇦🇿', url='https://t.me/zenmusiqi'),
                    InlineKeyboardButton('Qrupa əlavə et➕', url='https://t.me/song_azbot?startgroup=true')
                ]
            ]
        )
    )

        message.reply_audio(audio_file, reply_markup, caption=rep, parse_mode='md', title=title, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌Xəta\n\n Xətanı bildirmək üçün @abbasov1o ❤️')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@TG.on_message(filters.command("musiqi")&filters.group)
def a(client, message):
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
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

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
    m.edit(f"`{title[:35]}` yüklənir✅")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🇦🇿**{title[:35]}** | @song_azbot' 
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
            quote=False,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('PlayList🇦🇿', url='https://t.me/zenmusiqi'),
                    InlineKeyboardButton('Qrupa əlavə et➕', url='https://t.me/song_azbot?startgroup=true')
                ]
            ]
        )
    )
    
        message.reply_audio(audio_file, reply_markup, caption=rep, parse_mode='md', title=title, thumb=thumb_name)
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
