def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI)
    weight: kg
    height: cm
    """
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def calculate_calories(age, weight, height, gender, activity):
    """
    Calculate daily calorie needs using BMR
    """

    # Basal Metabolic Rate (Mifflin-St Jeor)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factor = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725
    }

    calories = bmr * activity_factor[activity]
    return round(calories)
