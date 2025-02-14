import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthCalculations(unittest.TestCase):

    def test_calculate_bmi(self):
        """Test du calcul de l'IMC."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)  # Hauteur 0 impossible
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, -70)  # Poids négatif impossible

    def test_calculate_bmr(self):
        """Test du calcul du BMR."""
        self.assertAlmostEqual(calculate_bmr(1.75, 70, 30, 'male'), 1695.36, places=2)
        self.assertAlmostEqual(calculate_bmr(1.75, 70, 30, 'female'), 1505.10, places=2)

        with self.assertRaises(ValueError):
            calculate_bmr(1.75, 70, 30, 'other')  # Genre invalide
        with self.assertRaises(ValueError):
            calculate_bmr(0, 70, 30, 'male')  # Hauteur invalide
        with self.assertRaises(ValueError):
            calculate_bmr(1.75, 0, 30, 'male')  # Poids invalide
        with self.assertRaises(ValueError):
            calculate_bmr(1.75, 70, 0, 'male')  # Âge invalide

if __name__ == '__main__':
    unittest.main()
