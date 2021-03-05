import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question95(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([12304, 2008, 1024, 2400, 120])
        self.second = random.choice([1,2,4])
        self.body = "{0} / {1} = ".format(self.first,self.second)
        self.res="{0}".format(self.first/self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
