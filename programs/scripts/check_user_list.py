# Checks entire twitch viewers user list on a timer
import requests

ALLOWLIST = ["CommanderRoot", "StreamElements", "Nightbot"]

bots_online_response = requests.get("https://api.twitchinsights.net/v1/bots/online")
bot_list = bots_online_response.json()['bots']

users_online_response = requests.get("https://tmi.twitch.tv/group/user/feathere_tv/chatters")
users_online_list = users_online_response.json()['chatters']['viewers']

# list of viewers online
# print(users_online_list)

# list of bots names
bot_names_list = []
for bot in bot_list:
    bot_names_list.append(bot[0])
# print(bot_names_list)

# remove allowlist names from list
for good_bot in map(str.lower, ALLOWLIST):
    bot_names_list.remove(good_bot.lower())
# print(bot_names_list)

users_online_list = ["kattah", "01ella"]

# for each user on list in bot_names_list, check if user is online bot list
for user in users_online_list:
    if user.lower() in map(str.lower, bot_names_list):
        # check if user is in viewer bot list, if yes, return user
        print(user)
    else:
        # do nothing
        print("User checks out 👍")

# debugging
# username = "kattah"
# print("first user on list: " + bot_list[0][0])
