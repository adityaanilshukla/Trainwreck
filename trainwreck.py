from start import *
from echo import *
from echolocation import *

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

    #print("From: " + str(context.) + "\nError: " + str(context.error) + "\n The update object was:\n" + str(update))
    print("Error: " + str(context.error) + "\n The update object was:\n" + str(update))

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
    #dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("echo", echo_command))
    dp.add_handler(MessageHandler(Filters.location & (~ Filters.update.edited_message), echolocation_command))
    dp.add_handler(MessageHandler(Filters.location & Filters.update.edited_message, echolocation_recovery_command))
    dp.add_error_handler(error_logging)
    job = updater.job_queue
    job.run_repeating(echolocation_job, interval = 10)
    updater.start_polling()
    updater.idle()

print("Bot is running =)")
main()