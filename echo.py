from globals_and_dependencies import *

def echo_command(update, context):

    """
    sends "echo" back lmao

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

    #update.message.reply_text("\uE29C85")
    update.message.reply_text("\U00002705")