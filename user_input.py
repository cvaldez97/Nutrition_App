from functions import *
from constants import *
from calculator import *

# --- User ---
def user_input():
        user = {}

        # --- Name ---
        type_text("Please enter your name: ", 0.05, new_line=False)
        user["name"] = input().strip().title()
        while not user["name"]:
            user["name"] = input("Please enter a valid name: ").strip().title()
        print("")

        # --- Sex Input ---   
        user["sex"] = get_confirmed_choice("Are you Male or Female?: ",sex_map)
        print("")

        # --- Weight, Height and Age Input ---
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
        "\nPlease make a selection: ", goal_map, confirm_key=True)

        # --- Goal Weight ---
        if user["goal"] == "maintain":
                user["goal_weight"] = user["weight"] 
        else: user["goal_weight"] = get_confirmed_number("\nWhat is your ideal weight in pounds?: ", float)
        print("")

        # --- Aggresion Calculation ---
        if user["goal"] != "maintain":
            user["aggression"] = get_confirmed_choice("How aggressive do you want to be?:" \
            "\n - Mild ... (0.5 pounds a week)." \
            "\n - Moderate ... (1.0 pound a week)." \
            "\n - Aggressive ... (1.5 pounds a week)." \
            "\n - Extreme ... (2.0 pounds a week). " \
            "\nPlease make a selection: ", aggression_map[user["goal"]], confirm_key=True)
            print("")
        
        # --- Activity Input ---
        user["activity"] = get_confirmed_choice("What is your level of activity?:"
            "\n- Sedentary ... (Little to no exercise)."
            "\n- Light ... (Light exercise 1-3 days/week)." 
            "\n- Moderate ... (exercise 3-5 days/week)." 
            "\n- Hard ... (exercise 6-7 days/week)." 
            "\n- Very Hard ... (training, physical labor, or 2x/day training). "
            "\nplease make a selection: ", activity_map)
        return user