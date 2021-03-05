import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question96(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([1,2,3,4,5])
        self.second = random.choice([6,7,8,9])
        self.third = random.choice([0,10,11,12])
        self.body = "{0} x {1} x {2} = ".format(self.first,self.second,self.third)
        self.res="{0}".format(self.first*self.second*self.third)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
