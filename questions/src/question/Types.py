from enum import Enum


class Types(Enum):
    Money_Got_Spent_Left = 1,
    Equation_First_order_one_unknown=2,
    Vehicle_speed_time_distance=3,
    Fraction_add=4,
    Fraction_compare=5,
    Fraction_simplify=6,
    Fraction_sub=7,
    Fraction_mul=8,
    Fraction_decimal=9,
    Time_add=10,
    Time_sub=11,
    Time_24hr_am_pm=12,
    Percentage=13,
    Power=14,
    Conversion=15,


class Complexity(Enum):
    Basic = 1,
    Moderate = 2,
    Advanced = 3,
    Complex = 4,


