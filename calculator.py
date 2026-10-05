from constants import aggression_map
from user_input import user_input

# --- Calculate User BMR ---
def calculate_bmr(weight, height, age, sex):
    weight_kg = weight / 2.2
    height_cm = height * 2.54
    sex = sex.strip().lower()
    if sex == "male":
        return(10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    elif sex == "female": 
        return(10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    else:
        raise ValueError("Invalid sex")

# --- Calculate User TDEE ---    
def calculate_tdee(bmr, activity):
    return(bmr * activity)

# --- Calculate User Calories ---
def target_calories(tdee, goal, aggression):
   if goal == "maintain":
       return tdee
   return tdee + aggression_map[goal][aggression]

# --- Calculate Protein ---
def target_protein(user):
    user["protein"] = user["goal_weight"]
    return user["protein]"]

def target_protein_cals(user):
    user["protein_cals"] = user["protein"] * 4
    return user["protein_cals"]

# --- Calculate Fat ---
def target_fat(user):
    user["fat"] = user["fat_cals"] / 9
    return user["fat"]
    
def target_fat_cals(user):
    user["fat_cals"] = user["calories"] * 0.3
    return user["fat_cals"]
    
# --- Calculate carbs ---
def target_carbs(user):
    user["carbs"] = user["carb_cals"] / 4
    return user["carbs"]

def target_carbs_cals(user):
    user["carb_cals"] = user["calories"] - (user["fat_cals"] + user["protein_cals"])
    return user["carb_cals"]
    