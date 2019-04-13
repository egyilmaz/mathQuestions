from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .utils.Utility import get_two_distinct


class Question28(BaseQuestion):
    def __init__(self):
        self.first, self.second = get_two_distinct([2,5,10,20,25,30,40,50,60,75,90,100])
        res1 = Fraction(self.first,100)
        res2 = Fraction(self.second,100)
        self.res = "{0}/{1} and {2}/{3}".format(res1.numerator,res1.denominator,res2.numerator,res2.denominator)
        self.body = "Represent {0}% and {1}% as fractions".format(self.first, self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
