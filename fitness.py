"""
# File: fitness.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Functions

"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender=input("Please enter your gender (M or F): ")
    birth_str=str(input("Enter your birthdate (YYYY-MM-DD): "))
    pounds=float(input("Enter your weight in U.S. pounds: " ))
    inches=float(input("Enter your height in U.S. inches: "))
    years=compute_age(birth_str)
    weight_kg=kg_from_lb(pounds)
    height_cm=cm_from_in(inches)
    bmi=body_mass_index(weight_kg, height_cm)
    bmr=basal_metabolic_rate(gender, weight_kg, height_cm, years)
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    print(f"Age: {abs(years)}")
    print(f"Weight (kg): {weight_kg:.2f}")
    print(f"Height (cm): {height_cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

    

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
        #years -= 3
    return years


def kg_from_lb(pounds):
    weight_kg=pounds*0.45359237
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return weight_kg


def cm_from_in(inches):
    height_cm=inches*2.54
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return height_cm


def body_mass_index(weight_kg, height_cm):
    bmi=(10000*weight_kg)/height_cm**2
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return bmi


def basal_metabolic_rate(gender, weight_kg, height_cm, years):
    if gender.upper()=="F":
       bmr_women=(447.593+(9.247*weight_kg))+(3.098*height_cm)-(4.33*years)
       bmr=round(bmr_women)
    else:
        bmr_men=88.362+(13.397*weight_kg)+(4.799*height_cm)-(5.677*years)
        bmr=round(bmr_men)
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    return bmr


# Call the main function so that
# this program will start executing.
main()