from asyncore import dispatcher
import keys
from telegram import (
    Bot
)


def img_command(update, context):

    """
    sends an image to the chat
    
    """
    chat_id = update.message.chat_id
    img = "images\chessboard.png"
    bot = Bot(keys.API_KEY)
    bot.send_photo(chat_id, photo=open(img, 'rb'))