# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 22, 2022

import unittest
from fitnessTrackerFuncs import *
class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertEqual(convert_lb_to_kg(170), 77.1107029)
        self.assertEqual(convert_lb_to_kg(200), 90.718474)

    def test_compute_MET(self):
        self.assertEqual(compute_MET(1), 5)
        self.assertEqual(compute_MET(4), 4)

    def test_compute_calorie_burned(self):
        self.assertEqual(compute_calorie_burned(90, 77, 7), 848.925)
        self.assertEqual(compute_calorie_burned(100, 90, 5), 787.5)

    def test_compute_BMI(self):
        self.assertEqual(compute_BMI(150, 60), 29.291666666666668)
        self.assertEqual(compute_BMI(170, 68), 25.845588235294116)

    def test_BMI_category(self):
        self.assertEqual(BMI_category(23), "Normal weight")
        self.assertEqual(BMI_category(26), "Overweight")

    def test_compute_equivalent_miles(self):
        self.assertEqual(compute_equivalent_miles(60, 3, 30), 1.1732954545454546)
        self.assertEqual(compute_equivalent_miles(68, 2, 60), 6.0369962121212115)


if __name__ == '__main__':
    unittest.main()
