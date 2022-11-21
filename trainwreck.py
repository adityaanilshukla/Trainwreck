import keys
from telegram.ext import *
from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    Bot
)
from start import *
from echo import *
from datetime import time as timer

bot = Bot(keys.API_KEY)
#individual_DB = IndividualSQite()
#group_DB = GroupSQlite()

print("Bot is running =)")
def error_logging(update, context):

    """
    Error logging: For internal Debugging.

    Parameters 
    ----------
    update: JSON file which calls the telegram command containing information about the user 
    context: An object that is mainly used for error handling (Read more here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html)

    Returns
    -------
        Displays the error message in the terminal console.
    
    """

    print("Update %s caused error %s" % (update, context.error))

def main():

    """
    Entry point function which setups the telegram bot and configure the telegram handlers.

    Parameters 
    ----------
    None

    Returns
    -------
    None
    
    """
    #individual_DB.setup()
    #group_DB.setup()
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("echo", echo_command))
    #dp.add_handler(CommandHandler("guess", guess_command))
    #dp.add_handler(CommandHandler("guess", guess_command))
    #dp.add_handler(CommandHandler("add", add_interest_command))
    #dp.add_handler(CommandHandler("remove", remove_interest_command))
    #dp.add_handler(CommandHandler("myinterest", my_interest_command))
    #dp.add_handler(CommandHandler("interest", interest_command))
    #dp.add_handler(CommandHandler("setup", setup_command))
    #dp.add_handler(CommandHandler("help", help_command))
    dp.add_error_handler(error_logging)
    job = updater.job_queue
    #job.run_daily(kick_users, time=timer(hour = 3, minute = 31, second = 00),days=(0, 1, 2, 3, 4, 5, 6))
    #job.run_daily(send_link, time=timer(hour = 3, minute = 31, second = 0),days=(0, 1, 2, 3, 4, 5, 6))
    updater.start_polling()
    updater.idle()

main()