import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question102(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([16,25,32,41,17,23,28,34])
        self.second = random.choice([421, 576, 123, 987, 617, 248])
        self.third = random.choice([423, 570, 231, 875, 728, 666])
        self.body = "{1} x {0} and {2} / {0} = ".format(self.first,self.second, self.first*self.third)
        self.res="{0} and {1}".format(self.first*self.second, self.third)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
