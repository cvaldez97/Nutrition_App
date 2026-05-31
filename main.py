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
type_text("Valdez Nutrition", 0.05)
type_text("-------------------", 0.1)
print("")

# Messaging functions
def greeting(name):
    return f"{name}, welcome to Valdez Nutrition"

def goal_confirm(name, path):
    return f"You have selected '{path}'. Is this correct?"

def sex_confirm(name, sex):
    return f"You have selected '{sex}'. Is this correct?"

def activity_confirm(name, activity):
    return f"{name}, you have selected '{activity}'. Is this correct?"

# --- Name Input ---
type_text("Please enter your name: ", 0.05, new_line=False)
name = input().strip().title()

while not name:
    name = input("Please enter a valid name: ").strip().title()

# --- Intro ---
print("")
type_text(greeting(name))
time.sleep(1)

type_text("Nutrition Made Simple.")
time.sleep(1)

print("")
type_text(f"{name}, lets get started with a few basic questions so that I can best assist you in your calorie and macro goals!", 0.05)
type_text("-------------------", 0.1)
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
        type_text(sex_confirm(name, sex))
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
        type_text(goal_confirm(name, path))
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
        age = float(input().strip())
        if age > 0:
            break
        else:
            type_text("Please enter a valid age.\n ")
    except ValueError:
        type_text("Numbers only.\n")

print("")

activity_map = {
    "1": "Little to no exercise.", 
    "2": "Light exercise 1-3 days/week.",
    "3": "Moderate exercise 3-5 days/week.",
    "4": "Hard exercise 6-7 days/week.",
    "5": "Very hard training, physical labor, or 2x/day traing."
}

while True:
    type_text("Based off of the options below how would you gauge your level of activity?:", 0.05)
    type_text("- 1: Little to no exercise."
    "\n- 2: Light exercise 1-3 days/week." 
    "\n- 3: Moderate exercise 3-5 days/week." 
    "\n- 4: Hard exercise 6-7 days/week." 
    "\n- 5: Very hard training, physical labor, or 2x/day training. ", 0.05)
    type_text("please make a numeric decision by selecting 1 -5: ", 0.05, new_line=False)
    activity_input = input().strip()
    
    if activity_input in activity_map:
        activity = activity_map[activity_input]
        print("")
        type_text(activity_confirm(name, activity))
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

type_text("One moment while I calculate your calories..")
type_text("-------------------", 0.1)
print("")

if sex == "female":
    BMR_F_equation(height, weight, age, activity)
else:
    MBMR = BMR_M_equation(weight, height, age, activity)

type_text(f"{name}'s Daily Calories\n - {MBMR}")

# Finish converting calories with activity for both male and female
# Next adjust calories based on goal path
# finally take final calories and convert them into macros
