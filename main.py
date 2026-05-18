# create user frienly options ( ft instead on inches, make an easy go back option )
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
# Intro load in
print("")
type_text("Valdez Nutrition", 0.05)
type_text("-------------------", 0.1)
print("")

# Messaging functions
def greeting(name):
    return f"{name}, welcome to Valdez Nutrition"

def goal_confirm(name, path):
    return f"{name}, you have selected '{path}'. Is this correct?"


# --- Name Input ---
type_text("Please enter your name: ", 0.05, new_line=False)
name = input().strip().title()

while not name:
    name = input("Please enter a valid name: ").strip().title()

# --- Intro ---
type_text(greeting(name))
time.sleep(1)

type_text("Nutrition Made Simple.")
time.sleep(1)


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


# --- Sex Input --- ### fix this stuff next 
type_text("Perfect. Let's move forward.")

while True:
    type_text(f"{name}, are you Male or Female?: ")
    sex_input = input().strip().lower()

    if "female" in sex_input:
        sex = "Female"
        break
    elif "male" in sex_input:
        sex = "Male"
        break
    else:
        type_text("Please include 'Male' or 'Female'.\n")


# --- Next Step ---
type_text(f"Perfect, {name}. I just need a few details to build your custom plan.\n")
time.sleep(0.5)
type_text("-------------------", 0.1)
print("")

while True:
    type_text("What's your weight (lbs)?: ", new_line=False)
    try:
        weight = float(input().strip())
        if weight > 0:
            break
        else:
            type_text("Enter a valid weight.\n")
    except ValueError:
        type_text("Numbers only.\n")

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
type_text("-------------------", 0.1)
print("")
        
type_text(f"\nAwesome {name}, I have your current weight at {weight}, height at {height}, and your age at {age}. ")
confirm = input("Is this correct? (yes/no): ").strip().lower() #make typewrite

while True:
    if confirm in ["yes", "y"]:
        break
    else:
        type_text("No problem, let's try that again.\n") #break infinite loop and make loop over details

