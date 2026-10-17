# Valdez Nutrition Calculator

A command-line calorie and macronutrient calculator written in Python. It asks for basic profile information, activity level, and a goal, then prints an estimated calorie and macro target.

## Requirements

- Python 3.12 or newer
- No third-party Python packages are required

## Run the calculator

Open a terminal in the project folder and run:

```bash
python3 main.py
```

Follow the prompts to enter age, weight in pounds, height in inches, goal, activity level, and contact details. The calculator checks the entered age, weight, and height against the ranges defined in `user_input.py`.

## Run the tests

From the project folder, run:

```bash
python3 -m unittest discover -s tests -v
```

## Calculation notes

- BMR uses the Mifflin–St Jeor equation with weight converted from pounds to kilograms using `2.2` and height converted from inches to centimeters using `2.54`.
- TDEE is estimated by multiplying BMR by the selected activity factor in `constants.py`.
- The calorie target applies a fixed daily calorie adjustment for the selected goal and aggression level.
- Protein is estimated at one gram per pound of goal weight. Fat is set to 30% of the calorie target. Remaining calories are assigned to carbohydrates.

These are estimates based on the assumptions and fixed values in the program; they are not individualized medical advice. The results depend on the accuracy of the entered information and the selected activity level.

## Project files

- `main.py` — starts the program and connects the input and report steps.
- `user_input.py` — collects and validates user input.
- `calculator.py` — contains BMR, TDEE, calorie, and macro calculations.
- `constants.py` — stores available choices and calculation factors.
- `summary_report.py` — calculates and displays the user's summary.
- `formatters.py` — formats height for display.
- `functions.py` — provides reusable prompt and confirmation helpers.
- `load_in.py` — displays the welcome message and typewriter text effect.
- `tests/test_calculator.py` — unit tests for the calculation functions.