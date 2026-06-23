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
    
def calculate_tdee(bmr, activity):
    return(bmr * activity)

def target_calories(tdee, goal):
   if goal == "Fat Loss":
       return tdee - 500
   if goal == "Build Muscle":
       return tdee + 250
   return tdee