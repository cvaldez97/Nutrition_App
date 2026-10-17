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


# --- Build Calculated Summary Data ---
def build_summary(user):
    bmr = round(calculate_bmr(
        user["weight"], user["height"], user["age"], user["sex"]
    ))
    tdee = round(calculate_tdee(bmr, user["activity"]))

    if user["goal"] == "maintain":
        calories = tdee
    else:
        calories = round(target_calories(
            tdee, user["goal"], user["aggression"]
        ))

    protein = round(target_protein(user["goal_weight"]))
    protein_calories = round(target_protein_cals(protein))
    fat_calories = round(target_fat_cals(calories))
    fat = round(target_fat(fat_calories))
    carb_calories = round(
        target_carbs_cals(calories, fat_calories, protein_calories)
    )
    carbs = round(target_carbs(carb_calories))

    return {
        "bmr": bmr,
        "tdee": tdee,
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
    }
