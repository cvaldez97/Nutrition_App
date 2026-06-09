import time
import sys
from formula import *

# Typewriter effect
def type_text(text, speed=0.05, new_line=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if new_line:
        print()

# Intro load in
print("")
type_text("Nutrition v.01", 0.05)
type_text("-------------------", 0.1)
print("")

# functions
def goal_confirm(path):
    return f"You have selected '{path}'. Is this correct?"

def sex_confirm(sex):
    return f"You have selected '{sex}'. Is this correct?"

def activity_confirm(activity):
    return f"{name}, you have selected '{activity}'. Is this correct?"

# --- Name Input ---
type_text("Please enter your name: ", 0.05, new_line=False)
name = input().strip().title()

while not name:
    name = input("Please enter a valid name: ").strip().title()

print("")

# --- Sex Input ---   
sex_map = {
    "male": "Male",
    "female": "Female",
    "m": "Male",
    "f": "Female"
}

while True:
    type_text("Are you Male or Female?: ", new_line=False)
    sex_input = input().strip().lower()

    if sex_input in sex_map:
        sex = sex_map[sex_input]
        print("")
        type_text(sex_confirm(sex))
        type_text("Type Yes or No: ", 0.05, new_line=False)
        confirm = input().strip().lower()

        if confirm in ["yes", "y"]:
            break
        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")
        else:
            type_text("Please type Yes or No only.\n")
    else:
        type_text("Please select a valid option.\n")

# --- Goal Selection ---
goal_map = {
    "fat loss": "Fat Loss",
    "build muscle": "Build Muscle",
    "maintain": "Maintain"
}

print("")

while True:
    type_text("Tell me your main goal:\n- Fat Loss\n- Build Muscle\n- Maintain")
    type_text("Please make a selection: ", 0.05, new_line=False) 
    path_input = input().strip().lower()

    if path_input in goal_map:
        path = goal_map[path_input]
        print("")
        type_text(goal_confirm(path))
        type_text("Type Yes or No: ", 0.05, new_line=False) 
        confirm = input().strip().lower()

        if confirm in ["yes", "y"]:
            break
        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")
        else:
            type_text("Please type Yes or No only.\n")
    else:
        type_text("Please select a valid option.\n")

print("")

# --- H, W, A ---
while True:
    type_text("How much do you weigh (lbs)?: ", new_line=False)
    try:
        weight = float(input().strip())
        if weight > 0:
            break
        else:
            type_text("Enter a valid weight.\n")
    except ValueError:
        type_text("Numbers only.\n")

print("")

while True:
    type_text("what's your height (inches)?: ", new_line=False)
    try: 
        height = float(input().strip())
        if height > 0: 
            break
        else: 
            type_text("Enter a valid height.\n")
    except ValueError:
        type_text("numbers only.\n")

print("")

while True:
    type_text("What is your current age?: ", new_line=False)
    try:
        age = int(input().strip())
        if age > 0:
            break
        else:
            type_text("Please enter a valid age.\n ")
    except ValueError:
        type_text("Numbers only.\n")

print("")

activity_map = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "hard": 1.725,
    "very_hard": 1.9
}

while True:
    type_text("What is your level of activity?:", 0.05)
    type_text("- sedentary ... (Little to no exercise)."
    "\n- light ... (Light exercise 1-3 days/week)." 
    "\n- moderate ... (exercise 3-5 days/week)." 
    "\n- hard ... (exercise 6-7 days/week)." 
    "\n- very hard ... (training, physical labor, or 2x/day training). ", 0.05)
    type_text("please make a selection: ", 0.05, new_line=False)
    activity_input = input().strip().lower()

    if activity_input in activity_map:
        activity = activity_map[activity_input]
        print("")
        type_text(activity_confirm(activity_input))
        type_text("Type Yes or No: ", 0.05, new_line=False) 
        confirm = input().strip().lower()

        if confirm in ["yes", "y"]:
            break
        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")
        else:
            type_text("Please type Yes or No only.\n")
    else:
        type_text("Please select a valid option.\n")

print("")
type_text("Calculating your calories now..", 0.05)
type_text("-------------------", 0.05)
bmr = calculate_bmr(weight, height, age, sex)
tdee = calculate_tdee(bmr, activity)
print("")
type_text(f"{name}'s macros:")
type_text("-------------------", 0.05)
type_text(f"bmr - {int(bmr)}")
type_text(f"tdee - {int(tdee)}")