from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
import logging
import texts
import handleAudioFile
import handleAudioMessage
import handleVideo
from telegram.ext import Updater
from dotenv import load_dotenv
import os

MESSAGE_TYPES = [handleVideo.MESSAGE_TYPE,
                 handleAudioFile.MESSAGE_TYPE, handleAudioMessage.MESSAGE_TYPE]

load_dotenv()  # take environment variables from .env.
token = os.getenv("TELEGRAM_BOT_TOKEN")
assert token is not None

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=texts.welcome_text)


def handleMessage(update, context):
    message = update.message
    chat = update.effective_chat
    action = next(filter(lambda x: x["condition"](
        message), MESSAGE_TYPES))["function"]
    action()


messageHandler = MessageHandler(~Filters.command, handleMessage)
dispatcher.add_handler(messageHandler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
