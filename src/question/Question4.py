import random
from src.resources.Resource import args, values, coeff


# Question type is Ax = B,
class Question4:
    def __init__(self, user_input):
        self.user_input = user_input
        self.body = "Given {coeff}{arg} = {result}."
        self.arg = random.choice(args)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.result = self.coeff * self.val

    def ask(self):
        first = self.user_input(self.arg)
        return first == self.val

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, result=self.result)
