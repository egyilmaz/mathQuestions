import random
from .utils.Utility import get_two_distinct
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question68(BaseQuestion):
    def __init__(self):
        self.type = Types.Decimal
        self.complexity = Complexity.Advanced
        self.oper = random.choice(['+','-','*'])
        self.dec1,self.dec2 = get_two_distinct([0.001, 0.2, 0.003, 1.04, 2.5, 2.06, 0.01, 0.0, 0.021, 3.002, 3.04, 40.0, 100.001])
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