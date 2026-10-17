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
    if goal not in aggression_map:
        raise ValueError("Invalid goal")
    if aggression not in aggression_map[goal]:
       raise ValueError("Invalid aggression level")
    cals = tdee  + aggression_map[goal][aggression]
    if cals <= 0:
        raise ValueError("Calories cannot be at or below 0")
    return cals

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
    if calories - (fat_cals + protein_cals) < 0:
        raise ValueError("Protein and fat calories exceed the calorie target")
    return calories - (fat_cals + protein_cals)

def target_carbs(carb_cals):
    return carb_cals / 4