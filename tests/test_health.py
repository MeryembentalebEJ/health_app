import unittest
from app.health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_bmi_calculation(self):
        self.assertEqual(calculate_bmi(1.75, 70), 22.86)  # Test simple pour le BMI

    def test_bmr_calculation_male(self):
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, "male"), 1724.05, places=2)  # Tolérance de 2 décimales

    def test_bmr_calculation_female(self):
        self.assertAlmostEqual(calculate_bmr(165, 60, 30, "female"), 1383.68, places=2)  # Tolérance de 2 décimales

if __name__ == '__main__':
    unittest.main()
