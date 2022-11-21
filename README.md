# Trainwreck
## Installation
### For developers
### For everyone else

# The secret lair
## Rick's priorities:
### Sunday:
- Command to delete all messages.
- For completed features, modify message behaviour so the bot edits messages instead of sending them.

###Moving forward:
- Reminder to refresh live location.
- SQlite bs
- Backend

## Knowldge dump
- It turns out that as a user you can't send a new message containing a live location while another one hasn't expired. During that time, there is only the option to stop updating the location of the current message. So my next idea is to remind users periodically at 2h, 1h and 30min left on the location, to delete and resend an 8h-live location at a convenient time. If at any point a location has not been shared for more than 1 minute I as the host will be notified. - Rick 22-11