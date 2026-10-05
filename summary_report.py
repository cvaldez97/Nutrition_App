from functions import type_text
from calculator import calculate_bmr, calculate_tdee, target_calories, target_protein, target_protein_cals, target_fat_cals, target_fat, target_carbs_cals, target_carbs

# --- User Summary Report ---
def summary_report(user):
    print("")
    type_text("Calculating your calories now..", 0.05)
    print("")
    user["bmr"] = round(calculate_bmr(user["weight"], user["height"], user["age"], user["sex"]))
    user["tdee"] = round(calculate_tdee(user["bmr"], user["activity"]))
    if user["goal"] != "maintain":
        user["calories"] = round(target_calories(user["tdee"], user["goal"], user["aggression"]))
    else:
          user["calories"] = user["tdee"]
    user["protein"] = round(target_protein(user["goal_weight"]))
    user["protein_calories"] = round(target_protein_cals(user["goal_weight"]))
    user["fat_calories"] = round(target_fat_cals(user["calories"]))
    user["fat"] = round(target_fat(user["fat_calories"]))
    user["carb_calories"] = round(target_carbs_cals(user["calories"], user["fat_calories"], user["protein_calories"])) 
    user["carbs"] = round(target_carbs(user["carb_calories"]))
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