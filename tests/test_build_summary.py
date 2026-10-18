import unittest
from calculator import build_summary

# python -m unittest discover -s tests -v
# ^^^ to run tests in root of project ^^^

class TestBuildSummary(unittest.TestCase):
    def make_user(self, goal):
        return {
            "weight": 180,
            "height": 70,
            "age": 30,
            "sex": "male",
            "activity": 1.2,
            "goal": goal,
            "goal_weight": 180,
            "aggression": "moderate",
        }

    def test_maintenance_goal(self):
        user = self.make_user("maintain")
        original_user = user.copy()

        summary = build_summary(user)

        self.assertEqual(user, original_user)
        self.assertEqual(summary["bmr"], 1784)
        self.assertEqual(summary["tdee"], 2141)
        self.assertEqual(summary["calories"], 2141)
        self.assertEqual(summary["protein"], 180)

    def test_fat_loss_goal(self):
        user = self.make_user("fat loss")
        original_user = user.copy()

        summary = build_summary(user)

        self.assertEqual(user, original_user)
        self.assertEqual(summary["calories"], 1641)
        self.assertEqual(summary["protein"], 180)

    def test_build_muscle_goal(self):
        user = self.make_user("build muscle")
        original_user = user.copy()

        summary = build_summary(user)

        self.assertEqual(user, original_user)
        self.assertEqual(summary["calories"], 2641)
        self.assertEqual(summary["protein"], 180)


if __name__ == "__main__":
    unittest.main()