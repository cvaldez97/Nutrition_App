from constants import aggression_map

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
def target_protein(goal_weight):
    return goal_weight

def target_protein_cals(protein):
    return protein * 4

# --- Calculate Fat ---
def target_fat_cals(calories):
    return calories * 0.3

def target_fat(fat_cals):
    return fat_cals / 9
    
# --- Calculate carbs ---
def target_carbs_cals(calories, fat_cals, protein_cals):
    return calories - (fat_cals + protein_cals)

def target_carbs(carb_cals):
    return carb_cals / 4