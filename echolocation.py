from globals_and_dependencies import *

def echolocation_command(update, context):

    """
    Adds a message containing a live location to the list of live locations. Other functions can get live location data from the list throughout the session.

    Parameters 
    ----------
    update: JSON file which calls the telegram command containing information about the user 
    context: An object that is mainly used for error handling (Read more here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html)

    Returns
    -------
    None
    
    """

    if update.message.location.live_period != 28800 :
        update.message.reply_text("Please share an 8-hour live location instead.")
        return

    # Remove live location from the list if it already exists
    for player in live_locations :
        if update.message.from_user.id == player[0] :
            live_locations.remove(player)
            break

    # Add new live location to the list
    live_locations.append((update.message.from_user.id, update.message.chat.id, update.message.message_id, update.message.date + datetime.timedelta(seconds = update.message.location.live_period)))
    bot.unpin_all_chat_messages(live_locations[0][1])
    bot.pinChatMessage(live_locations[0][1], live_locations[0][2])
    #if os.path.exists("lobbyState.txt") :

    #    # Read
    #    lobby_state_file = open("lobbyState.txt", "r")
    #    lobby_state = lobby_state_file.read()
    #    lobby_state_file.close()

    #    # User ID, message_id, chat_id, expiry date (date + live_period)
    #    lobby_state = str(live_locations[0][0]) + ", " + str(live_locations[0][1]) + ", " + str(live_locations[0][2]) + ", " + str(live_locations[0][3])
    #    # TODO: Check if live location from user ID already exists, and if so, replace instead of add.

    #    # Write
    #    lobby_state_file = open("lobbyState.txt", "w")
    #    lobby_state_file.write(lobby_state)
    #    lobby_state_file.close()
    #else : # Remove this afterwards lol
    #    lobby_state_file = open("lobbyState.txt", "w")
    #    lobby_state_file.close()
    
    update.message.reply_text("\U00002705 Location shared!")

def echolocation_recovery_command(update, context):

    """
    In the possibility that the bot crashes and has to be restarted, this one-time function allows the bot to recover a player's chat on their next live location refresh.
    This way, the bot continues to maintain service within 10 seconds of coming back up, without the player's involvement.
    In practice, all live location refreshes are sent here regardless of the bot's status, but nothing is done unless the bot hasn't registered the user, which usually happens when the bot has just restarted.

    Parameters 
    ----------
    update: JSON file which calls the telegram command containing information about the user 
    context: An object that is mainly used for error handling (Read more here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html)

    Returns
    -------
    None
    
    """

    # TODO: Once lobbies are implemented, check if this player belongs to any lobby.

    # Don't do anything if the list already contains the player.
    for player in live_locations :
        if update.edited_message.from_user.id == player[0] :
            return

    pinned_message = bot.getChat(update.edited_message.chat.id).pinned_message
    live_locations.append((pinned_message.from_user.id, pinned_message.chat.id, pinned_message.message_id, pinned_message.date + datetime.timedelta(seconds = pinned_message.location.live_period)))

def echolocation_job(context: CallbackContext):

    """
    Sends a message every 10 seconds of a user's live location coordinates. Proof of concept on how to use live location data in other functions. May be deleted.

    Parameters 
    ----------
    context: An object that is mainly used for error handling (Read more here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html)

    Returns
    -------
    None
    
    """

    # Read
    #lobby_state_file = open("lobbyState.txt", "r")
    #lobby_state = lobby_state_file.read()
    #lobby_state_file.close()

    for player in live_locations :
        # Get the message from the chat and message ID's.
        if (bot.getChat(player[1]).pinned_message != None) : 
            location = bot.getChat(player[1]).pinned_message.location
            bot.send_message(player[1], str(location.latitude) + ", " + str(location.longitude))