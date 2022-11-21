#from individual_sqlite import *
#from tag import *
import os
import datetime
from telegram.ext import *
from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    Bot,
)
from datetime import time as timer

import keys

#individual_DB = IndividualSQite()
bot = Bot(keys.API_KEY)
live_locations = []