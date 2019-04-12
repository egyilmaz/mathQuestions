import random
from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .Types import Types
from ..resources.Resource import random_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct, descending

class Question28(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.first, self.second = get_two_distinct([2,5,10,20,25,30,40,50,60,75,90,100])
        res1 = Fraction(self.first,100)
        res2 = Fraction(self.second,100)
        self.res = "{0}/{1} and {2}/{3}".format(res1.numerator,res1.denominator,res2.numerator,res2.denominator)
        self.body = "Represent {0}% and {1}% as fractions".format(self.first, self.second)

    def question(self):
        return self.body

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
