import random
from .Types import Types
from ..resources.Resource import args, values, coeff
from ..utils.Utility import ask_interactive_1arg


# Question type is Ax = B,
class Question4:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.arg = random.choice(args)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.res = self.coeff * self.val
        self.body = "Given {coeff}{arg} = {res}.".format(coeff=self.coeff, arg=self.arg, res=self.res)
        self.question_text = "What is {arg} ?".format(arg=self.arg)

    def question(self):
        return self.body + ' ' + self.question_text

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.arg: self.val}

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)
