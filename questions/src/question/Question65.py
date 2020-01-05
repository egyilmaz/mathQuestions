import random
from fractions import Fraction
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question65(BaseQuestion):
    def __init__(self):
        self.type = Types.Ratio
        self.complexity = Complexity.Moderate
        self.cls = random.choice([20,30,40])
        self.foreign  = random.choice([2,3,4,5,10])
        self.body = "In a class of {cls} students. Only {pupils} are foreign nationals."\
                "What is the ratio of these foreign nationals to the whole class? What is the ratio of "\
                "the foreign nationals to the rest of the students?".format(cls=self.cls, pupils = self.foreign)
        self.ratio1 = Fraction(self.foreign,self.cls)
        self.ratio2 = Fraction(self.foreign,self.cls-self.foreign)

    def question(self):
        return self.body

    def answer(self):
        return "{0}:{1} and {2}:{3}".format(self.ratio1.numerator,self.ratio1.denominator,
                                        self.ratio2.numerator,self.ratio2.denominator)
