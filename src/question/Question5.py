import random
from src.resources.Resource import args, consts, coeff, values


# Question type is Ax + B = C,
class Question5:
    def __init__(self, user_input):
        self.user_input = user_input
        self.body = "Given {coeff}{arg} + {const} = {result}."
        self.arg = random.choice(args)
        self.const = random.choice(consts)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.result = self.coeff * self.val + self.const

    def ask(self):
        first = self.user_input(self.arg)
        return first == self.val

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, result=self.result, const=self.const)
