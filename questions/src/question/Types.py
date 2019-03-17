from enum import Enum


class Types(Enum):
    FIRST_ORDER_2_UNKNOWN = 1
    FIRST_ORDER_1_UNKNOWN = 2


class Output(Enum):
    PRINTED = 1  # printing questions and answers to file per sheet
    ONLINE = 2 # asking the questions only
    INTERACTIVE = 3 # asking the questions and getting the user input()

