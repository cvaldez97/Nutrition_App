from functions import type_text
from calculator import calculate_bmr, calculate_tdee, target_calories, target_protein, target_protein_cals, target_fat_cals, target_fat, target_carbs_cals, target_carbs
from constants import goal_map
from formatters import format_height

# --- User Summary Report ---
def summary_report(user):
    print("")
    user["bmr"] = round(calculate_bmr(user["weight"], user["height"], user["age"], user["sex"]))
    user["tdee"] = round(calculate_tdee(user["bmr"], user["activity"]))
    if user["goal"] != "maintain":
        user["calories"] = round(target_calories(user["tdee"], user["goal"], user["aggression"]))
    else:
          user["calories"] = user["tdee"]
    user["protein"] = round(target_protein(user["goal_weight"]))
    user["protein_calories"] = round(target_protein_cals(user["protein"]))
    user["fat_calories"] = round(target_fat_cals(user["calories"]))
    user["fat"] = round(target_fat(user["fat_calories"]))
    user["carb_calories"] = round(target_carbs_cals(user["calories"], user["fat_calories"], user["protein_calories"])) 
    user["carbs"] = round(target_carbs(user["carb_calories"]))
    type_text("-------------------")
    type_text("Valdez Nutrition")
    type_text("Nutrition Blueprint")
    type_text("-------------------")
    print("")
    type_text(f"Client: {user["name"]}")
    type_text(f"Email: {user["email"]}")
    print("")
    type_text(f"Goal: {goal_map[user["goal"]]}")
    type_text(f"Goal Weight: {int(user["goal_weight"])} lb")
    print("")
    type_text("Current Metrics:")
    type_text(f"Sex: {user["sex"]}")
    type_text(f"Weight: {int(user["weight"])} lb")
    type_text(format_height(user["height"]))
    type_text(f"Age: {user["age"]}")
    print("")
    type_text(f"Calorie Target: {int(user["calories"])} Calories")
    print("")
    type_text("Macros:")
    type_text(f"Protein: {user["protein"]}g")
    type_text(f"Carbohydrates: {user["carbs"]}g")
    type_text(f"Fat: {user["fat"]}g")
    print("")
    type_text("Coach Notes")
    type_text("**place holder**")
    print("")
    type_text("-------------------")
    type_text("VALDEZ NUTRITION")
    type_text("NUTRITION. MADE. SIMPLE.")
    type_text("-------------------")