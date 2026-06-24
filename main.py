from calculator import *
from functions import *
from constants import *

# Intro load in
print("")
type_text("Nutrition v1", 0.05)
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

print("")
# --- weight, height and age input ---
age = get_confirmed_number("What is your age?: ",int)
print("")
weight = get_confirmed_number("What is your weight in pounds?: ",float)
print("")
height = get_confirmed_number("What is your height in inches?: ",float)

print("")
# --- Goal Selection ---
goal = get_confirmed_choice("Tell me your main goal:" 
"\n- Fat Loss" 
"\n- Build Muscle" 
"\n- Maintain" 
"\nPlease make a selection: ", goal_map, goal_confirm)

if goal == "Maintain":
        goal_weight = weight 
else: goal_weight = get_confirmed_number("\nwhat is your ideal weight in pounds?: ", float)
    
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
# --- Summary report ---
type_text("Calculating your calories now..", 0.05)
print("")
bmr = calculate_bmr(weight, height, age, sex)
tdee = calculate_tdee (bmr, activity)
calories = target_calories(tdee, goal)
protein = (f"{round(goal_weight)}" + "g")
protein_calories = (round(goal_weight * 4))
fat_calories = round(calories * 0.3)
fat = (f"{round(fat_calories / 9)}") + "g"
carb_calories = round(calories - (fat_calories + protein_calories)) 
carbs = (f"{round(carb_calories / 4)}") + "g"
type_text("-------------------" "\nclient summary" "\n-------------------")
print("")
type_text(f"Name: {name}")
print("")
type_text(f"Sex: {sex}")
type_text(f"Age: {age}")
type_text(f"Weight: {weight}")
type_text(f"Height: {height}")
print("")
type_text(f"Goal: {goal}")
type_text(f"Goal Weight: {goal_weight}")
print("")
type_text(f"BMR: {int(bmr)}")
type_text(f"Caloreis: {int(calories)}")
print("")
type_text("Macros: ")
type_text(f"Protein: {protein}" + " / " f"{protein_calories}" + " calories")
type_text(f"Fat: {fat}" + " / " + f"{fat_calories}" + " calories")
type_text(f"Carbohydrates: {carbs}" + " / " + f"{carb_calories}" + " calories")
print("")
type_text("*** Macros are rounded up to the nearest gram. ***")
type_text("-------------------")