import unittest
from calculator import calculate_bmr, calculate_tdee, target_calories, target_protein, target_protein_cals, target_fat, target_fat_cals, target_carbs, target_carbs_cals

# python -m unittest discover -s tests -v
# ^^^ to run tests in root of project ^^^

# --- Test BMR Calculation ---
class TestCalculateBMR(unittest.TestCase):
    def test_calculate_bmr_male(self):
        result = calculate_bmr(220, 73, 29, "male")
        self.assertAlmostEqual(result, 2017, delta=2)
    
    def test_calculate_bmr_female(self):
        result = calculate_bmr(220, 73, 29, "female")
        self.assertAlmostEqual(result, 1851, delta=2)
    
    def test_calculate_bmr_invalid_sex(self):
        with self.assertRaises(ValueError):
            result = calculate_bmr(220, 73, 29, "unkown")
            self.assertAlmostEqual(result, ValueError)

# --- Test TDEE Calculation ---
class TestCalculateTDEE(unittest.TestCase):
    def test_calculate_tdee_moderate_activity(self):
        result = calculate_tdee(2000, 1.55)
        self.assertAlmostEqual(result, 3100)

# --- Test Target Calories ---
class TestTargetCalories(unittest.TestCase):
    def test_target_calories_maintain_weight_moderate(self):
        result = target_calories(2500, "maintain weight", "moderate")
        self.assertAlmostEqual(result, 2500)
    
    def test_target_calories_lose_weight_moderate(self):
        result = target_calories(2500, "lose weight", "moderate")
        self.assertEqual(result, 2000)

    def test_target_calories_invalid_goal(self):
        with self.assertRaises(ValueError):
            result = target_calories(2500, "invalid goal", "moderate")
            self.assertRaises(result, ValueError)

    def test_target_calories_invalid_aggression(self):
        with self.assertRaises(ValueError):
            result = target_calories(2500, "lose weight", "very aggressive")
            self.assertRaises(result, ValueError)

    def test_target_calories_gain_weight_moderate(self):
        result = target_calories(2500, "gain weight", "moderate")
        self.assertAlmostEqual(result, 3000)

    def test_target_calories_lose_weight_extreme(self):
        result = target_calories(2500, "lose weight", "extreme")
        self.assertAlmostEqual(result, 1500)

    def test_target_calories_if_calories_is_below_0(self):
        with self.assertRaises(ValueError):
            target_calories(700, "lose weight", "extreme")

# --- Test Protein Calculations ---
class TestProteinCalculations(unittest.TestCase):
    def test_target_protein(self):
        result = target_protein(200)
        self.assertAlmostEqual(result, 200)

    def test_target_protein_cals(self):
        result = target_protein_cals(200)
        self.assertAlmostEqual(result, 800)

# --- Test Fat Calculations ---
class TestFatCalculations(unittest.TestCase):
    def test_target_fat(self):
        result = target_fat(600)
        self.assertAlmostEqual(result, 67, delta=1)

    def test_target_fat_calories(self):
            result = target_fat_cals(2000)
            self.assertAlmostEqual(result, 600)

# --- Test Carbohydrates Calculation ---
class TestCarbohydratesCalculation(unittest.TestCase):
    def test_target_carbs(self):
        result = target_carbs(600)
        self.assertAlmostEqual(result, 150)

    def test_target_carbs_cals(self):
        result = target_carbs_cals(2000, 600, 800)
        self.assertAlmostEqual(result, 600)

    def test_target_carbs_cals_negative_result(self):
        with self.assertRaises(ValueError):
            result = target_carbs_cals(1200, 600, 800)
            self.assertAlmostEqual(result, ValueError)
