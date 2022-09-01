# Project 1 Fitness Tracking
#
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 22, 2022

# purpose: Introduce the project to the participant
# signature: none --> str
def welcome():
    print("To begin you must specify the participant's name,")
    print("age, height (in inches), weight (in lb), exercise ")
    print("duration (in minutes), and exercise type (1-4)! Now ")
    print("you can compote the burned calories and BMI")


# purpose: Participant inputs their name for the system
# signature: none --> str
def input_name():
    name = input("Enter the name: ")
    return name


# purpose: Participant inputs their age for the system
# signature: none --> int
def input_age():
    age = int(input("Enter age: "))
    while age <= 0:
        print("age must be an integer > 0!")
        age = int(input("Enter age: "))
    return age


# purpose: Participant inputs their height for the system
# signature: none --> int
def input_height():
    height = int(input("Enter height in inches: "))
    while height <= 0:
        print('height must be greater 0!')
        height = int(input("Enter height in inches: "))
    return height


# purpose: Participant inputs their weight for the system
# signature: none --> int
def input_weight():
    weight = int(input("Enter weight in lb: "))
    while weight <= 0:
        print("weight must be greater 0!")
        weight = int(input("Enter weight in lb: "))
    return weight


# purpose: Participant inputs the amount they work out for the system
# signature: none --> int
def input_duration():
    duration = int(input("Enter duration of exercise in minutes: "))
    while duration <= 0:
        print("duration must be greater 0!")
        duration = int(input("Enter duration of exercise in minutes: "))
    return duration


# purpose: Participant inputs their type of exercise for the system
# signature: none --> int
def input_exercise_type():
    type_exercise = int(input("Enter exercise type, 1) Low-impact 2) High-impact 3) Slow-paced 4) Fast-paced: "))
    while type_exercise < 1 or type_exercise > 4:
        print("exercise type must be an integer between [1,4]!")
        type_exercise = int(input("Enter exercise type [1, 4]: "))
    return type_exercise


# purpose: Writes out all the info that the participant put in
# signature: strintfloatfloatfloatfloatfloat -> strintfloatfloatfloatfloatfloat
def print_info(name, age, height, weight, calorie_burned, BMI, miles):
    print("%18s %5s" % ("Name = ", name))
    print("%18s %3d" % ("Age = ", age))
    print("%18s %3.00f %5s" % ("Height = ", height, "inches"))
    print("%18s %2.00f %2s" % ("Weight = ", weight, "lb"))
    print("%18s %4.00f" % ("Miles = ", miles))
    print("%18s %2.02f" % ("Burned Calories = ", calorie_burned))
    print("%18s %2.02f" % ("BMI = ", BMI))


# purpose: Get weight from lb to kg
# signature: float -> float
def convert_lb_to_kg(weight):
    weight_kg = weight * 0.45359237
    return weight_kg


# purpose: Matches exercise type with MET
# signature: int -> int
def compute_MET(exercise_type):
    if exercise_type == 1:
        return 5
    elif exercise_type == 2:
        return 7
    elif exercise_type == 3:
        return 3
    elif exercise_type == 4:
        return 4


# purpose: Takes amount worked weight and MET to calculate how many calories are lost
# signature: floatfloatint -> float
def compute_calorie_burned(duration, weight, met_value):
    calorie_burned = (duration * (met_value * 3.5 * (weight * 0.45359237)) / 200)
    return calorie_burned


# purpose: Uses weight and height to calculate BMI
# signature: floatfloat -> float
def compute_BMI(weight, height):
    BMI = (703 * weight / (height ** 2))
    return BMI


# purpose: Takes your BMI and tells you what category you're in
# signature: float -> str
def BMI_category(BMI):
    if BMI < 18.59:
        return "Underweight"
    elif BMI <= 18.59 or BMI < 24.99:
        return "Normal weight"
    elif BMI <= 25 or BMI < 29.99:
        return "Overweight"
    elif BMI >= 30:
        return "Obesity"


# purpose: Takes in time height and exercise type to calculate miles ran
# signature: floatintfloat -> float
def compute_equivalent_miles(height, exercise_type, duration):
    if exercise_type == 1:
        miles = ((((0.413 * height) / 12) * (120 * duration)) / 5280)
        return miles
    elif exercise_type == 2:
        miles = ((((0.413 * height) / 12) * (227 * duration)) / 5280)
        return miles
    elif exercise_type == 3:
        miles = ((((0.413 * height) / 12) * (100 * duration)) / 5280)
        return miles
    elif exercise_type == 4:
        miles = ((((0.413 * height) / 12) * (152 * duration)) / 5280)
        return miles
