import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import args, values, coeff
from .Types import Types, Complexity


# Question type is Ax = B,
class Question4(BaseQuestion):
    def __init__(self):
        self.type = Types.First_order_one_unknown
        self.complexity = Complexity.Basic
        self.arg = random.choice(args)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.res = self.coeff * self.val
        self.body = "Given {coeff}{arg} = {res}.".format(coeff=self.coeff, arg=self.arg, res=self.res)
        self.question_text = "What is {arg} ?".format(arg=self.arg)

    def question(self):
        return self.body + ' ' + self.question_text

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)
