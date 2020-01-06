import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from sympy.ntheory import factorint


class Question112(BaseQuestion):
    def __init__(self):
        self.type = [Types.Factors, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        number = random.choice([40, 50, 90, 100,120,243,75, 125, 490, 1210, 64, 1000])
        self.body = "Find the prime factors of {0}".format(number)
        self.res="{0}".format(factorint(number, multiple=True))

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
