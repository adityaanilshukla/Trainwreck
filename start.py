#from individual_sqlite import *
#from tag import *

#individual_DB = IndividualSQite()
def start_command(update, context):

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

    if chat_type == "group" or chat_type == "supergroup":

        info_public_group_text = "This command only works in private chat.\nTo join Social Travellers's matching queue, you can private message the bot with /start."
        update.message.reply_text(info_public_group_text)

    else:
        text = str(update.message.text).lower().split()
    
        if len(text) > 2:
            tag_to_update = ""
            invalid_tags = ""
            text.remove('/start')
            for i in text:
                if i in tags:
                    tag_to_update+= "%s " %i
                else:
                    invalid_tags+= "%s " %i
            failure_add_tags = "\nThe following tag(s) are invalid: %s." % invalid_tags
            if len(tag_to_update) != 0:
                
                # Need to add into db
                #individual_DB.add_chatID_tags(user_char_id, tag_to_update)
                success_add_new_user_tag = "Have successfully added you into SocialTravellers's Queue."
                if len(invalid_tags) != 0:
                    
                    update.message.reply_text(success_add_new_user_tag + failure_add_tags)
                else:
                    update.message.reply_text(success_add_new_user_tag)
            else:
                failure_add_new_user_tag_no_tags = "Failed to add you into SocialTravellers's Queue."
                update.message.reply_text(failure_add_new_user_tag_no_tags + failure_add_tags)
        
        else:
            info_private_group_text = 'Hi, please select any 5 of the following Interest tags:\n'
            for interest in tags:
                info_private_group_text += interest + '\n'
            update.message.reply_text(info_private_group_text)
