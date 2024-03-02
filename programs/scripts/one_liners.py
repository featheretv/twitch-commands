from datetime import datetime
import random
import re
import sys
import textwrap

# Change the location for your list of pickup lines
CAT_FACTS_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/cat_facts.txt'
DAD_JOKES_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/dad_jokes.txt'
DOG_FACTS_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/dog_facts.txt'
DIARY_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/diary.txt'
PICKUP_LINES_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/pickup_lines.txt'
STORY_TIME_FILE_PATH = 'C:/Users/eunic/IdeaProjects/twitch-commands/programs/resources/storytime.txt'

NUMERICAL_DATE_FORMAT = '%m-%d-%Y'
FULL_MONTH_DATE_FORMAT = '%B %d, %Y'
BIRTHDATE = datetime(1986, 3, 15)

# Set channel point redemption type
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
    case "Story":
        file_to_read = STORY_TIME_FILE_PATH
    case _:
        file_to_read = ''


def calculate_age(date_object):
    return date_object.year - BIRTHDATE.year - ((date_object.month, date_object.day) < (BIRTHDATE.month, BIRTHDATE.day))


# Open the file in read mode
with open(file_to_read, "r", encoding="utf8") as file:
    all_text = file.read()
    line = list(map(str, all_text.split("\n")))
    random_line = random.choice(line)

    match(sys.argv[1]):
        case "Diary":
            # Regex to parse, search, and grab date from the first 20 characters per diary entry line
            pattern = r'^(?P<date>\w+\s+\d{1,2},\s+\d{4})'  # Define regex pattern <date>
            match = re.search(pattern, random_line[:20])
            matched_date = match.group('date')
            diary_date = datetime.strptime(matched_date, FULL_MONTH_DATE_FORMAT)
            age = calculate_age(diary_date)
            print(textwrap.fill(random_line, 485) + ' (' + str(age) + ' years old)')
        case "Story":
            story_date = datetime.strptime(random_line[:10], NUMERICAL_DATE_FORMAT)
            age = calculate_age(story_date)
            # Print from beginning of txt file without date
            print(textwrap.fill(random_line[11:], 485) + ' (' + str(age) + ' years old)')
        case _:
            print(textwrap.fill(random_line, 500))
