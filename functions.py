from load_in import type_text

# --- Confirm User Goal Input ---
def get_confirmed_choice(prompt, options_map, confirm_key=False):
    while True:
        type_text(prompt, new_line=False)
        user_input = input().strip().lower()
        if user_input not in options_map:
            type_text("Please select a valid option.\n")
            continue
        choice = options_map[user_input]
        print("")
        confirmation_value = user_input 
        type_text(f"You have selected '{confirmation_value}'. Is this correct?")
        type_text("Type Yes or No: ", new_line=False)
        confirm = input().strip().lower()
        if confirm in ["yes", "y"]:
            return user_input if confirm_key else choice
        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")
        else:
            type_text("Please type Yes or No only.\n")

# --- Confirm User Number Input ---
def get_confirmed_number(prompt, number_type=float):
    while True:
        type_text(prompt, new_line=False)
        try:
            value = number_type(input().strip())
        except ValueError:
            type_text("Please enter a valid number.\n")
            continue
        type_text(f"You entered '{value}'. Is this correct?")
        type_text("Type Yes or No: ", new_line=False)
        confirm = input().strip().lower()
        if confirm in ["yes", "y"]:
            return value
        elif confirm in ["no", "n"]:
            type_text("Alright, let's try again...\n")
        else:
            type_text("Please type Yes or No only.\n")