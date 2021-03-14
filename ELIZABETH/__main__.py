import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async



@run_async
def ppchi(bot: Bot, update: Update):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]

    if chat.type == "private":
        update.effective_message.reply_photo(DEVIL_IMG, reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="Help",url="t.me/{}?start=help".format(bot.username))],  
                                                [InlineKeyboardButton(text="Creater",url="https://t.me/the_noobhacker")]]),disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
    
