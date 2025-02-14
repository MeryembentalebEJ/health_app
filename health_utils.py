def calculate_bmi(height, weight):
    """Calcule l'IMC (BMI)."""
    if height <= 0 or weight <= 0:
        raise ValueError("La taille et le poids doivent être supérieurs à zéro.")
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    """Calcule le métabolisme de base (BMR) selon la formule de Harris-Benedict."""
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("La taille, le poids et l'âge doivent être supérieurs à zéro.")

    height_cm = height * 100  # Conversion en cm

    if gender == "male":
        return round(88.36 + (13.4 * weight) + (4.8 * height_cm) - (5.7 * age), 2)
    elif gender == "female":
        return round(447.6 + (9.2 * weight) + (3.1 * height_cm) - (4.3 * age), 2)
    else:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
