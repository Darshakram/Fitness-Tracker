# Main Program
# Project 1 Fitness Tracking
#
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 22, 2022
from fitnessTrackerFuncs import *


def main():
    welcome()
    while True:
        name = input_name()
        age = input_age()
        height = input_height()
        weight = input_weight()
        duration = input_duration()
        exercise_type = input_exercise_type()
        weight_kg = convert_lb_to_kg(weight)
        met_value = compute_MET(exercise_type)
        calorie_burned = compute_calorie_burned(duration, weight, met_value)
        BMI = compute_BMI(weight, height)
        miles = compute_equivalent_miles(height, exercise_type, duration)
        info = print_info(name, age, height, weight, calorie_burned, BMI, miles)
        print("%18s %5s" % ("BMI Category = ", BMI_category(BMI)))
        question = str(input("Do you want to appy fitness tracking for another user (y/n)?"))
        print(question)
        if question == "n":
            break
        elif question != "y":
            return True


if __name__ == '__main__':
    main()


def enter_side():
    side_length = int(input("Value of a side of a square:  "))


def square_area(side):
    area = int(input("value"))
    return area ** 2
