import unittest
from unittest.mock import patch
from user_input import user_input

# python -m unittest discover -s tests -v
# ^^^ to run tests in root of project ^^^

class TestGoalWeightValidation(unittest.TestCase):
    def test_lose_weight_rejects_goal_weight_above_current_weight(self):
        # Choices: sex, goal, aggression, activity level
        with patch("user_input.get_confirmed_choice") as choices:
            choices.side_effect = ["Male", "lose weight", "moderate", 1.2]

            # Numbers: age, current weight, height,
            # then an invalid and valid goal weight
            with patch("user_input.get_confirmed_number") as numbers:
                numbers.side_effect = [30, 180, 70, 190, 170]

                # Pretend name and email were entered
                with patch("builtins.input", side_effect=["Casey", "casey@example.com"]):
                    with patch("user_input.type_text"):
                        user = user_input()

        self.assertEqual(user["goal_weight"], 170)
        self.assertEqual(numbers.call_count, 5)

    def test_gain_weight_rejects_goal_weight_below_current_weight(self):
        with patch("user_input.get_confirmed_choice") as choices:
            choices.side_effect = ["Male", "gain weight", "moderate", 1.2]

            with patch("user_input.get_confirmed_number") as numbers:
                numbers.side_effect = [30, 180, 70, 170, 190]

                with patch("builtins.input", side_effect=["Casey", "casey@example.com"]):
                    with patch("user_input.type_text"):
                        user = user_input()

        self.assertEqual(user["goal_weight"], 190)
        self.assertEqual(numbers.call_count, 5)


if __name__ == "__main__":
    unittest.main()
