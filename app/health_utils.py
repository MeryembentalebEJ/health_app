def calculate_bmi(height, weight):
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    if gender == "male":
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    elif gender == "female":
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
    else:
        raise ValueError("Invalid gender")
