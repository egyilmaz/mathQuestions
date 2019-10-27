import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question97(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([110.99, 23.928, 34.1, 41.9])
        self.second = random.choice([0.657, 0.2, 0.125, 0.001, 1.99, 2.99, 12.99, 21.99])
        self.body = "{0} + {1}  and {0} - {1} = ".format(self.first,self.second)
        self.res="{0} and {1}".format(self.first+self.second, self.first - self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
