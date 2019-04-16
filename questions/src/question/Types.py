from enum import Enum


class Types(Enum):
    Fraction_Got_Spent_Left = 1,
    First_order_one_unknown=2,
    Vehicle_speed_time_distance=3,
    Fraction_add=4,
    Fraction_compare=5,
    Fraction_simplify=6,
    Percentage=7,
    Power=8,
    Fraction_sub=9,
    Fraction_mul=10,
    Fraction_decimal=11,
    Time_add=12,
    Time_sub=13,
    Time_24hr_am_pm=14,


class Complexity(Enum):
    Basic = 1,
    Moderate = 2,
    Advanced = 3,
    Complex = 4

class Output(Enum):
    PRINTED = 1  # printing questions and answers to file per sheet
    ONLINE = 2 # asking the questions only
    INTERACTIVE = 3 # asking the questions and getting the user input()

