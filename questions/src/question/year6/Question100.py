import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question100(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([30, 40, 60, 70, 80])
        self.second = random.choice([120, 140, 150, 200, 240, 250])
        self.third = random.choice([120, 140, 150, 200, 240, 250])
        self.body = "{0}% x {1} and {0}% of {2} = ".format(self.first,self.second,self.third)
        self.res="{0} and {1}".format((self.first*self.second)/100, (self.first*self.third)/100)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
