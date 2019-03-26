import random
from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .Types import Types
from ..resources.Resource import random_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct, descending

class Question26(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.first, self.second = get_two_distinct( random_fractions )
        self.res = self.first * self.second 
        self.body = "Calculate   "

    def question(self):
        return self.body

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}  \ast  \dfrac{{{2}}}{{{3}}}$'.format(self.first.numerator,self.first.denominator,self.second.numerator,self.second.denominator)
        return self.encode_graphics(a)


    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
