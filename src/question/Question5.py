import random
from src.question.Types import Types
from src.resources.Resource import args, consts, coeff, values


# Question type is Ax + B = C,
class Question5:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.body = "Given {coeff}{arg} + {const} = {res}."
        self.arg = random.choice(args)
        self.question_text="What is {arg} ?".format(arg=self.arg)
        self.const = random.choice(consts)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.res = self.coeff * self.val + self.const

    def result(self):
        return {self.arg: self.val}

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, res=self.res, const=self.const)
