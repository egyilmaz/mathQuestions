from enum import Enum


class Types(Enum):
    Money_Got_Spent_Left = 1,
    Equation_First_order_one_unknown=2,
    Equation_First_order_two_unknown=3,
    Equation_Second_order_one_unknown=4,
    Equation_Second_order_two_unknown=5,
    Vehicle_speed_time_distance=6,
    Fraction_add=7,
    Fraction_compare=8,
    Fraction_simplify=9,
    Fraction_sub=10,
    Fraction_mul=11,
    Fraction_decimal=12,
    Time_add=13,
    Time_sub=14,
    Time_24hr_am_pm=15,
    Percentage=16,
    Power=17,
    Conversion=18,
    Geometry_circle_perimeter=19,


class Complexity(Enum):
    Basic = 1,
    Moderate = 2,
    Advanced = 3,
    Complex = 4,


