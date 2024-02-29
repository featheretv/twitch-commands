import random
import sys
import textwrap

# Change the location for your list of pickup lines
CAT_FACTS_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/cat_facts.txt'
DAD_JOKES_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/dad_jokes.txt'
DOG_FACTS_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/dog_facts.txt'
DIARY_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/diary.txt'
PICKUP_LINES_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/pickup_lines.txt'

# Switch statement
match sys.argv[1]:
    case "Cat Facts":
        file_to_read = CAT_FACTS_FILE_PATH
    case "Dad Jokes":
        file_to_read = DAD_JOKES_FILE_PATH
    case "Diary":
        file_to_read = DIARY_FILE_PATH
    case "Dog Facts":
        file_to_read = DOG_FACTS_FILE_PATH
    case "Pickup Lines":
        file_to_read = PICKUP_LINES_FILE_PATH
    case _:
        file_to_read = ''

# Open the file in read mode
with open(file_to_read, "r", encoding="utf8") as file:
    all_text = file.read()
    line = list(map(str, all_text.split("\n")))

    # Print random line from text file
    print(textwrap.fill(random.choice(line), 500))
