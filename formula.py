# Both formulas will take height in inches and convert it to cenimeters and weight in pounds and convert to kilograms within the functions. 

# Male Formula 
def BMR_M_equation(weight, height, age, activity):
    if activity == "Little to no exercise.":
        activity = 1.2
    elif activity == "Light exercise 1-3 days/week.":
        activity = 1.375
    elif activity == "Moderate exercise 3-5 days/week.":
        activity = 1.55
    elif activity == "Hard exercise 6-7 days/week.":
        activity = 1.725
    else:
        activity = 1.9
    bmr = (10 * (weight / 2.2)) + (6.25 * (height * 2.54)) - (5 * age) + 5
    return int(bmr * activity)

# Female equation 
def BMR_F_equation(weight, height, age, activity):
    if activity == "Little to no exercise.":
        activity = 1.2
    elif activity == "Light exercise 1-3 days/week.":
        activity = 1.375
    elif activity == "Moderate exercise 3-5 days/week.":
        activity = 1.55
    elif activity == "Hard exercise 6-7 days/week.":
        activity = 1.725
    else:
        activity = 1.9
    bmr = (10 * (weight / 2.2)) + (6.25 * (height * 2.54)) - (5 * age) - 161
    return int(bmr * activity)
    