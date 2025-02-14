def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI).
    
    BMI Formula: weight (kg) / (height (m) ** 2)

    :param height: Height in meters
    :param weight: Weight in kilograms
    :return: Rounded BMI value
    :raises ValueError: If inputs are invalid (negative or zero)
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    
    return round(weight / (height ** 2), 2)


def calculate_bmr(height, weight, age, gender):
    """
    Calculate the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.

    BMR Formula:
        - Male:    BMR = 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)
        - Female:  BMR = 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)

    :param height: Height in cm
    :param weight: Weight in kg
    :param age: Age in years
    :param gender: Gender ('male' or 'female')
    :return: Rounded BMR value
    :raises ValueError: If inputs are invalid
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive numbers.")

    if gender not in ["male", "female"]:
        raise ValueError("Gender must be 'male' or 'female'.")

    if gender == "male":
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    else:  # gender == "female"
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
