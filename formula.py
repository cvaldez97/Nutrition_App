# Both formulas will take height in inches and convert it to cenimeters and weight in pounds and convert to kilograms
# within the functions. 

# Male Formula 
def BMR_M_equation(weight, height, age, activity):
    return ((10 * (weight / 2.2)) + (6.25 * (height * 2.54)) - (5 * age) + 5) * activity
# ---example formula to test if it works. Delete when ready to deploy-----
weight = 220
height = 73
age = 29
activity = 1

BMR = int(BMR_M_equation(weight, height, age, activity))
print(BMR)

# Female equation 
def BMR_F_equation(weight, height, age, activity):
    return ((10 * (weight / 2.2)) + (6.25 * (height *2.54)) - (5 * age) - 161) * activity
# ---example formula to test if it works. Delete when ready to deploy-----
weight = 135
height = 60
age = 25
activity = 1

BMR = int(BMR_F_equation(weight, height, age, activity))
print (BMR)

# need to make a function that will convert BMR into macros
# Function below will take your BMR and convert it to your macros via protein, fat and carbs. 

    
