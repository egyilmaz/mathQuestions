import random
from src.question.Types import Types
from src.resources.Resource import args, values, coeff


# Question type is Ax = B,
class Question4:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.body = "Given {coeff}{arg} = {res}."
        self.arg = random.choice(args)
        self.question_text = "What is {arg} ?".format(arg=self.arg)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.res = self.coeff * self.val

    def result(self):
        return {self.arg: self.val}

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, res=self.res)
