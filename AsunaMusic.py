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

from pydub import AudioSegment
from json import dumps
from .shazam_helper.communication import recognize_song_from_signature
from .shazam_helper.algorithm import SignatureGenerator
from requests import get
from os import remove

import os
from config import Config

TG = Client(
    'AsunaMusic',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

def a():
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
    m.edit(f"`{title}` yüklənir✅")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🇦🇿**{title}**\n🎶Xoş Dinləmələr \n\n✅Yüklədi: [Song🇦🇿](https://t.me/song_azbot) \n↗️PlayList: [Toxun🎵](https://t.me/zenmusiqi)' 
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
    m.edit(f"`{title}` yüklənir✅")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🇦🇿**{title}**\n🎶Xoş Dinləmələr \n\n✅Yüklədi: [Song🇦🇿](https://t.me/song_azbot) \n↗️PlayList: [Toxun🎵](https://t.me/zenmusiqi)' 
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


@TG.on_message(filters.command("shazam")&filters.private)
async def shazam(event):
    if not event.is_reply:
        return await event.edit('`Zəhmət olmasa bir səsə cavab verin!`')
    else:
        await event.edit('`⬇️ Səs faylı yüklənir...`')
        reply_message = await event.get_reply_message()
        dosya = await reply_message.download_media()

        await event.edit('`🛠 Səs faylı fingerprint formasına çevrilir...`')
        audio = AudioSegment.from_file(dosya)
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
            
        signature_generator = SignatureGenerator()
        signature_generator.feed_input(audio.get_array_of_samples())
            
        signature_generator.MAX_TIME_SECONDS = 12
        if audio.duration_seconds > 12 * 3:
            signature_generator.samples_processed += 16000 * (int(audio.duration_seconds / 2) - 6)
            
        results = '{"error": "Not found"}'
        sarki = None
        await event.edit('`🎧 🎤 Shazamlanır...`')
        while True:
            signature = signature_generator.get_next_signature()
            if not signature:
                sarki = results
                break
            results = recognize_song_from_signature(signature)
            if results['matches']:
                sarki = results
                break
            else:
                await event.edit(f'`İlk {(signature_generator.samples_processed / 16000)} saniyədə heçnə tapılmadı... Birazda yoxlayıram...`')
        
        if not 'track' in sarki:
            return await event.edit('`Təsüfki Shazam verdiyiniz səsi tapa bilmədi ☹️ Daha aydın səs ata bilərsiz?`')
        await event.edit('`✅ Mahnını tapdım! Məlumatlar gətirilir...`')
        Caption = f'**Mahnı:** [{sarki["track"]["title"]}]({sarki["track"]["url"]})\n'
        if 'artists' in sarki['track']:
            Caption += f'**Sənətçilər(lər):** [{sarki["track"]["subtitle"]}](https://www.shazam.com/artist/{sarki["track"]["artists"][0]["id"]})\n'
        else:
            Caption += f'**Sənətçi(lər):** `{sarki["track"]["subtitle"]}`\n'

        if 'genres'in sarki['track']:
            Caption += f'**Növ:** `{sarki["track"]["genres"]["primary"]}`\n'

        if sarki["track"]["sections"][0]["type"] == "SONG":
            for metadata in sarki["track"]["sections"][0]["metadata"]:
                Caption += f'**{"İl" if metadata["title"] == "Sorti" else metadata["title"]}:** `{metadata["text"]}`\n'

        Caption += '\n**Mahnı Platformaları:** '
        for provider in sarki['track']['hub']['providers']:
            if provider['actions'][0]['uri'].startswith('spotify:track'):
                Url = provider['actions'][0]['uri'].replace(
                    'spotify:track:', 'http://open.spotify.com/track/'
                )
            elif provider['actions'][0]['uri'].startswith('intent:#Intent;action=android.media.action.MEDIA_PLAY_FROM_SEARCH'):
                Url = f'https://open.spotify.com/search/' + urllib.parse.quote(sarki["track"]["subtitle"] + ' - ' + sarki["track"]["title"])
            elif provider['actions'][0]['uri'].startswith('deezer'):
                Url = provider['actions'][0]['uri'].replace(
                    'deezer-query://', 'https://'
                )
            else:
                Url = provider['actions'][0]['uri']
            Caption += f'[{provider["type"].capitalize()}]({Url}) '
        for section in sarki['track']['sections']:
            if section['type'] == 'VIDEO':
                if 'youtubeurl' in section:
                    Youtube = get(section['youtubeurl']).json()
                else:
                    return

                Caption += f'\n**Klip Videosu:** [Youtube]({Youtube["actions"][0]["uri"]})'

        if 'images' in sarki["track"] and len(sarki["track"]["images"]) >= 1:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                sarki["track"]["images"]["coverarthq"] if 'coverarthq' in sarki["track"]["images"] else sarki["track"]["images"]["background"],
                caption=Caption,
                reply_to=reply_message
                )
        else:
            await event.edit(Caption)  
        remove(dosya)


TG.run()
