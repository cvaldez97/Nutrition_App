import time
import sys

# Typewriter effect
def type_text(text, speed=0.05, new_line=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if new_line:
        print()

def goal_confirm(path):
    return f"You have selected '{path}'. Is this correct?"

def sex_confirm(sex):
    return f"You have selected '{sex}'. Is this correct?"

def activity_confirm(activity):
    return f"You have selected '{activity}'. Is this correct?"

def get_confirmed_choice(prompt, options_map, confirm_function, confirm_key=False):

    while True:
        type_text(prompt, new_line=False)
        user_input = input().strip().lower()

        if user_input not in options_map:
            type_text("Please select a valid option.\n")
            continue

        choice = options_map[user_input]

        print("")

        confirmation_value = user_input if confirm_key else choice
        type_text(confirm_function(confirmation_value))

        type_text("Type Yes or No: ", new_line=False)
        confirm = input().strip().lower()

        if confirm in ["yes", "y"]:
            return choice

        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")

        else:
            type_text("Please type Yes or No only.\n")

def get_confirmed_number(prompt, number_type=float):
    while True:
        type_text(prompt, new_line=False)

        try:
            value = number_type(input().strip())
        except ValueError:
            type_text("Please enter a valid number.\n")
            continue

        type_text(f"You entered '{value}'. Is this correct?")

        type_text("Type Yes or No: ", new_line=False)
        confirm = input().strip().lower()

        if confirm in ["yes", "y"]:
            return value

        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")

        else:
            type_text("Please type Yes or No only.\n")