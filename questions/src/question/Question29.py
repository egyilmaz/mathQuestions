import random
from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .Types import Types
from ..resources.Resource import random_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct, descending

class Question29(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.first, self.second = get_two_distinct([2,5,10,20,25,30,40,50,60,75,90,100])
        self.res = [float(Fraction(self.first,100)),float(Fraction(self.second,100))] 
        self.body = "Represent {0}% and {1}% as decimals".format(self.first, self.second)

    def question(self):
        return self.body

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
