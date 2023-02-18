import keys
from telegram import (
    Bot
)
import teams

bot = Bot(keys.API_KEY)

# global lists where we store the usernames of each member
global red_players
red_players = []
global blue_players
blue_players = []
global observers
observers = []

def add_player_toTeam(userInput, context):

    """
    adds player to either red or blue team based on player input
    """
    # define variables used in deciding team
    chat_id = userInput.message.chat_id
    team = userInput.message.text
    chat_type = userInput.message.chat.type
    userName = userInput.message.chat.username

    #only add player if it is a private chat with the bot
    if(chat_type == "private" ):

        # only proceed if user is not a member of red team already
        if(team == "/red" and userName not in red_players ): 
            
            # player wants to move from blue to red team
            if(userName in blue_players):
                blue_players.remove(userName)
                red_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left blue team and joined red team")
            
            # player wants to move from observer to red team
            elif(userName in observers):
                observers.remove(userName)
                red_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left observers and joined red team")
            
            else: #player is not in any other team and is joining red team
                red_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you have been added to the red team")

            
        
        # only proceed if user is not a member of blue team already
        elif(team == "/blue" and userName not in blue_players ): 
            
            # player wants to move from red to blue team
            if(userName in red_players):
                red_players.remove(userName)
                blue_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left red team and joined blue team")
            
            # player wants to move from observer to blue team
            elif(userName in observers):
                observers.remove(userName)
                blue_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left observers and joined blue team")
            
            else: #player is not in any other team and is joining blue team
                blue_players.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you have been added to the blue team")
                
        # only proceed if user is not an observer already
        elif(team == "/observer" and userName not in observers ):

            # player wants to move from red team to observers
            if( userName in red_players):
                red_players.remove(userName)
                observers.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left red team and became an observer")
            
            # player wants to move from blue team to observers
            elif(userName in blue_players):
                blue_players.remove(userName)
                observers.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you left blue team and became an observer")

            else: #player is not in any other team and is joining observers
                observers.append(userName)
                bot.send_message(chat_id, "@"+userName+ " you have become an observer")

    else: #user was not in private chat
        return


    



