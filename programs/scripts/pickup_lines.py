import random

# Change the location for your list of pickup lines
PICKUP_LINES_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/pickup_lines.txt'

# Open the file in read mode
with open(PICKUP_LINES_FILE_PATH, "r") as file:
    all_text = file.read()
    line = list(map(str, all_text.split("\n")))

    # Print random line from text file
    print(random.choice(line))
