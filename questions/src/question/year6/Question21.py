import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question21(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Basic
        self.num = 10*random.choice(range(1, 10))
        self.per = 10*random.choice(range(1, 10))
        self.res = self.num*self.per/100
        self.body = "Find {per}% of {num}".format(num=self.num, per=self.per)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
