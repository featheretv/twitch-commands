# Python code to pick a random
# word from a text file
import random

# Open the file in read mode
with open("C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/PickUpLines.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split("\n")))

    # print random string
    print(random.choice(words))
