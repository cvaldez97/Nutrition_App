from calculator import *
from functions import *
from constants import *

# Intro load in
print("")
type_text("Nutrition v.01", 0.05)
type_text("-------------------", 0.1)
print("")

# --- Name Input ---
type_text("Please enter your name: ", 0.05, new_line=False)
name = input().strip().title()

while not name:
    name = input("Please enter a valid name: ").strip().title()

print("")
# --- Sex Input ---   
sex = get_confirmed_choice("Are you Male or Female?: ",sex_map, sex_confirm)

# --- Goal Selection ---
print("")

path = get_confirmed_choice("Tell me your main goal:" 
"\n- Fat Loss" 
"\n- Build Muscle" 
"\n- Maintain" 
"\nPlease make a selection: ", goal_map, goal_confirm)
    
print("")
# --- weight, height and age input ---
age = get_confirmed_number("What is your age?: ",int)
print("")
weight = get_confirmed_number("What is your weight in pounds?: ",float)
print("")
height = get_confirmed_number("What is your height in inches?: ",float)

print("")
# -- activity input --
activity = get_confirmed_choice("What is your level of activity?:"
    "\n- sedentary ... (Little to no exercise)."
    "\n- light ... (Light exercise 1-3 days/week)." 
    "\n- moderate ... (exercise 3-5 days/week)." 
    "\n- hard ... (exercise 6-7 days/week)." 
    "\n- very hard ... (training, physical labor, or 2x/day training). "
    "\nplease make a selection: ", activity_map, activity_confirm, confirm_key=True)

print("")
type_text("Calculating your calories now..", 0.05)
bmr = calculate_bmr(weight, height, age, sex)
tdee = calculate_tdee(bmr, activity)
print("")
type_text(f"{name}'s macros:")
type_text("-------------------", 0.05)
type_text(f"bmr - {int(bmr)}")
type_text(f"tdee - {int(tdee)}")