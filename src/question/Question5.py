import random
from src.question.Types import Types
from src.resources.Resource import args, consts, coeff, values
from src.utils.Utility import ask_interactive_1arg


# Question type is Ax + B = C,
class Question5:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
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

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.arg: self.val}

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)
