import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question94(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic, Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([12304,2005, 1024, 2613, 4325, 1203, 9898])
        self.second = random.choice([1000,100,10])
        self.body = "{0} - {1} = ".format(self.first,self.second)
        self.res="{0}".format(self.first-self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
