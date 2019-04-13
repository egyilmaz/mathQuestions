import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import args, consts, coeff, values


# Question type is Ax + B = C,
class Question5(BaseQuestion):
    def __init__(self):
        self.arg = random.choice(args)
        self.const = random.choice(consts)
        self.coeff = random.choice(coeff)
        self.val = random.choice(values)
        self.res = self.coeff * self.val + self.const
        self.body = "Given {coeff}{arg} + {const} = {res}."\
            .format(coeff=self.coeff, arg=self.arg, res=self.res, const=self.const)
        self.question_text = "What is {arg} ?".format(arg=self.arg)

    def question(self):
        return self.body + ' ' + self.question_text

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)
