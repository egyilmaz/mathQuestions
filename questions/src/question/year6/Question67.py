import random
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question67(BaseQuestion):
    def __init__(self):
        self.type = Types.Decimal
        self.complexity = Complexity.Moderate
        self.oper = random.choice(['+','-','*'])
        self.dec1,self.dec2 = get_two_distinct([0.01,0.02,0.03,0.04,0.5,0.6,1.0,2.1,3.2,3.4])
        if self.oper == '+':
            self.res = self.dec1 + self.dec2
        if self.oper == '-':
            self.res = self.dec2 - self.dec1
        if self.oper == '*':
            self.res = self.dec1*self.dec2
        self.body = "Calculate {0} {1} {2} = ?".format(self.dec2, self.oper, self.dec1)

    def question(self):
        return self.body

    def answer(self):
        return "{0}".format(self.res)