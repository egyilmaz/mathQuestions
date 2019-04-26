import random
from .utils.Utility import get_two_distinct
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity

def get_decimal_question( ):
    oper = random.choice(['+', '-'])
    dec1, dec2 = get_two_distinct([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0])
    res=0.0
    if oper == '+':
        res = dec1 + dec2
    if oper == '-':
        res = dec2 - dec1
    body = "{0} {1} {2}".format(dec2, oper, dec1)
    return res,body

class Question66(BaseQuestion):
    def __init__(self):
        self.type = Types.decimal
        self.complexity = Complexity.Basic
        self.res1,q1 = get_decimal_question()
        self.res2,q2 = get_decimal_question()
        self.body = "Calculate ({0}) and ({1})".format(q1, q2)

    def question(self):
        return self.body

    def answer(self):
        return "{0}, {1}".format(self.res1,self.res2)