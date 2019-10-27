import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question98(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([10, 100, 1000, 10000])
        self.second = random.choice([30, 40, 50, 60, 120, 150])
        self.third = random.choice([427, 540, 448, 284, 482, 1234])
        self.body = "{2} / {0}  and {1} * {1} = ".format(self.first,self.second,self.third)
        self.res = "{0} and {1}".format(self.third/self.first, self.second * self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
