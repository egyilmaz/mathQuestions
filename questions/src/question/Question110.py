import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question110(BaseQuestion):
    def __init__(self):
        self.type = [Types.Decimal, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        double = random.sample([0.01,0.02,0.03,0.04,0.05,0.06,0.07],3)
        triple = random.sample([0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007],3)
        result = round(double[0]+triple[0],4)
        asked = double+triple
        random.shuffle(asked)
        self.body = "Which two of the {0} adds up to {1}".format(asked, result )

        self.res="{0} and {1}".format(double[0], triple[0])

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
