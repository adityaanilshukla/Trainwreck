# Trainwreck
## Installation
### For developers
### For everyone else

# The secret lair
## Rick's priorities:
Ask if you'd like to take any tasks from me!
### Friday:
- Command to delete all messages.

### Saturday:
- Lobby registration functionality that saves chat IDs for all members.
- Use PILLOW to draw over a source image so the bot can send timely map updates.

### Moving forward:
- For completed features, modify message behaviour so the bot edits messages instead of sending them.
- Reminder to refresh live location.
- SQlite bs
- Backend

## Knowledge dump
- It turns out that as a user you can't send a new message containing a live location while another one hasn't expired. During that time, there is only the option to stop updating the location of the current message. So my next idea is to remind users periodically at 2h, 1h and 30min left on the location, to delete and resend an 8h-live location at a convenient time. If at any point a location has not been shared for more than 1 minute I as the host will be notified. - Rick 22-11
- A bot cannot initiate a conversation anywhere. It has to be added to a group, and users made to message it. With this in mind, I propose this registration workflow:
    1. The bot is added to a group and made to start with parameters.

        Any user: "@Trainwreck_Bot /help lobby"\
        *\*Bot sends message on the format to use to register a lobby. Let's say, timezone and game length in hours, separated by space.*\*\
        User A: "@Trainwreck_Bot /lobby 8 9"
    2. The bot has all the participants DM it a random number to confirm their participation. Any amount of observers can join, and upon joining they are given a reminder to preserve the integrity of the game by refraining from providing info to the players.

        *"**@User A**, DM me "450" within 60 seconds to create the lobby, or "/cancel"."*\
        \*User A DMs the bot "450".\*\
        *"Registration\
        Observers:\
        Team Red (0/2):\
        Team Blue (0/2):\
        DM me "225" to join Team Red, "420" to join Team Blue and "747" to be an observer. DM "/leave" to leave a team. The host may DM "/cancel"."*\
        \*Users A and F register as observers, while users B and C register in Team Red and users D and E, Team Blue. The host has the option of changing team names via DM.\*\
        *"Preparation\
        Observers:\
        **@User A** (host)\
        **@User F**\
        Team Red (2/2):\
        **@User B** :cross:\
        **@User C** :cross:\
        Team Blue (2/2):\
        **@User D** :cross:\
        **@User E** :cross:\
        DM me "225" to join Team Red, "420" to join Team Blue and "747" to be an observer. DM "/leave" to leave a team. The host may DM "/cancel"."*
    3. All players are given via DM a checklist of tasks to perform in order to be deemed ready in the lobby. The message is edited with ticks and crosses depending on what has been fulfilled.

        *"Please perform these tasks to be deemed ready:\
        :tick: Send an 8h live location\
        :cross: Be within 50m/56yd of your teammate (ensure you have both shared your live location)"*
    4. When everyone is ready, the lobby message is edited to reflect the start time of the game, which is in 5 minutes by default. The host is notified via DM and has the option to "/start" now, "/delay" by 5 minutes or to the next hour mark, or "/cancel". Any member turning unready will reset the lobby back to step 3.
    5. Once the game starts, it cannot be canceled and no more changes can be made. - Rick 28-11
