#from individual_sqlite import *
#from tag import *

#individual_DB = IndividualSQite()
def echo_command(update, context):

    """
    Starts the bot and add the user chat id and the valid interest tags into the individual database sqlite.
    If the command is ran in private chat, the bot will scape off the interest tags from the user input and validate it before adding into database.
    If the command is ran in group or supergroup, the bot will inform users to run it in private chat.

    Parameters 
    ----------
    update: JSON file which calls the telegram command containing information about the user 
    context: An object that is mainly used for error handling (Read more here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html)

    Returns
    -------
    None
    
    """
    grp_chat_id = update.message.chat_id 
    msg_chat_id = update.message.message_id
    chat_type = update.message.chat.type
    user_char_id = update.effective_user.id

    update.message.reply_text("echo")