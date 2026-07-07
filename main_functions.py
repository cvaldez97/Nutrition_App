from helper_functions import *
from constants import *
from calculator import *

def load_in():
        print("")
        print("")
        type_text("Nutrition v1", 0.05)
        type_text("-------------------", 0.1)
        print("")

def user_input():
        user = {}
        
        type_text("Please enter your name: ", 0.05, new_line=False)
        user["name"] = input().strip().title()

        while not user["name"]:
            user["name"] = input("Please enter a valid name: ").strip().title()

        print("")
        # --- Sex Input ---   
        user["sex"] = get_confirmed_choice("Are you Male or Female?: ",sex_map, sex_confirm)

        print("")
        # --- weight, height and age input ---
        user["age"] = get_confirmed_number("What is your age?: ",int)
        print("")
        user["weight"] = get_confirmed_number("What is your weight in pounds?: ",float)
        print("")
        user["height"] = get_confirmed_number("What is your height in inches?: ",float)

        print("")
        # --- Goal Selection ---
        user["goal"] = get_confirmed_choice("Tell me your main goal:" 
        "\n- Fat Loss" 
        "\n- Build Muscle" 
        "\n- Maintain" 
        "\nPlease make a selection: ", goal_map, goal_confirm, confirm_key=True)

        if user["goal"] == "maintain":
                user["goal_weight"] = user["weight"] 
        else: user["goal_weight"] = get_confirmed_number("\nwhat is your ideal weight in pounds?: ", float)

        #if user["goal"] != "maintain":
            #user["aggression"] = get_confirmed_choice("how aggressive do you want to be?: ", goal_map[user["goal"]], goal_confirm, confirm_key=True)
        
        print("")
        # -- activity input --
        user["activity"] = get_confirmed_choice("What is your level of activity?:"
            "\n- sedentary ... (Little to no exercise)."
            "\n- light ... (Light exercise 1-3 days/week)." 
            "\n- moderate ... (exercise 3-5 days/week)." 
            "\n- hard ... (exercise 6-7 days/week)." 
            "\n- very hard ... (training, physical labor, or 2x/day training). "
            "\nplease make a selection: ", activity_map, activity_confirm, confirm_key=True)
        return user
    
def summary_report(user):
    print("")
    type_text("Calculating your calories now..", 0.05)
    print("")
    user["bmr"] = round(calculate_bmr(user["weight"], user["height"], user["age"], user["sex"]))
    user["tdee"] = round(calculate_tdee(user["bmr"], user["activity"]))
    user["calories"] = round(target_calories(user["tdee"], user["goal"]))
    user["protein"] = round(user["goal_weight"])
    user["protein_calories"] = (round(user["goal_weight"] * 4))
    user["fat_calories"] = round(user["calories"] * 0.3)
    user["fat"] = round(user["fat_calories"] / 9)
    user["carb_calories"] = round(user["calories"] - (user["fat_calories"] + user["protein_calories"])) 
    user["carbs"] = round(user["carb_calories"] / 4)
    type_text("-------------------" "\nclient summary" "\n-------------------")
    print("")
    type_text(f"Name: {user["name"]}")
    print("")
    type_text(f"Sex: {user["sex"]}")
    type_text(f"Age: {user["age"]}")
    type_text(f"Weight: {user["weight"]}")
    type_text(f"Height: {user["height"]}")
    print("")
    type_text(f"Goal: {user["goal"]}")
    type_text(f"Goal Weight: {user["goal_weight"]}")
    print("")
    type_text(f"BMR: {int(user["bmr"])}")
    type_text(f"Calories: {int(user["calories"])}")
    print("")
    type_text("Macros: ")
    type_text(f"Protein: {user["protein"]}g" + " / " f"{user["protein_calories"]}" + " calories")
    type_text(f"Fat: {user["fat"]}g" + " / " + f"{user["fat_calories"]}" + " calories")
    type_text(f"Carbohydrates: {user["carbs"]}g" + " / " + f"{user["carb_calories"]}" + " calories")
    print("")
    type_text("*** Macros are rounded up to the nearest gram. ***")
    type_text("-------------------")