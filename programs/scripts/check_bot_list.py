import requests
import sys

ALLOW_LIST = ["CommanderRoot", "Nightbot", "Sery_Bot", "StreamElements"]

# This url looks at the first 15 entries
# bots_online_response = requests.get("https://api.twitchinsights.net/v1/bots/online")
# bots_online_list = bots_on_response.json()['bots']
# print(bots_online_list)

# This url looks at more bots
bots_all_response = requests.get("https://api.twitchinsights.net/v1/bots/all")
bot_list = bots_all_response.json()['bots']

# List of viewers online
# print(users_online_list)

# Parse response to save the list of bots names
bot_names_list = []
for bot in bot_list:
    bot_names_list.append(bot[0].lower())
# print(bot_names_list)

# Remove allowed bots from bot_names_list (if found)
for good_bot in ALLOW_LIST:
    bot_names_list.remove(good_bot.lower())
# print(bot_names_list)

# Check if viewer is in bot_names_list. If yes, return 1 for viewer found
if sys.argv[1].lower() in bot_names_list:
    print(1)
else:
    # Do nothing
    print(0)
