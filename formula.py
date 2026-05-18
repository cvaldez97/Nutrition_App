# Both formulas will take height in inches and convert it to cenimeters and weight in pounds and convert to kilograms
# within the functions. 

# Male Formula 
def BMR_M_equation(W, H, A):
    return (10 * (W / 2.2)) + (6.25 * (H * 2.54)) - (5 * A) + 5
# ---example formula to test if it works. Delete when ready to deploy-----
W = 220
H = 73
A = 29

BMR = int(BMR_M_equation(W, H, A))
print(BMR)

# Female equation 
def BMR_F_equation(W, H, A):
    return (10 * (W / 2.2)) + (6.25 * (H *2.54)) - (5 * A) - 161
# ---example formula to test if it works. Delete when ready to deploy-----
W = 135
H = 60
A = 25

BMR = int(BMR_F_equation(W, H, A))
print (BMR)

# need to make a function that will convert BMR into macros
# need to also find a way to convert BMR more accuratley based off of level of physical activity. 
# Function below will take your BMR and convert it to your macros via protein, fat and carbs. 

    
