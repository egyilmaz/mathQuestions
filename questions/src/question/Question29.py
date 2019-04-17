from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question29(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Basic
        self.first, self.second = get_two_distinct([2,5,10,20,25,30,40,50,60,75,90,100])
        self.res = [float(Fraction(self.first,100)),float(Fraction(self.second,100))] 
        self.body = "Represent {0}% and {1}% as decimals".format(self.first, self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
