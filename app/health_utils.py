def calculate_bmi(height, weight):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive numbers.")
    if gender not in ["male", "female"]:
        raise ValueError("Gender must be 'male' or 'female'.")

    if gender == "male":
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    else:
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
