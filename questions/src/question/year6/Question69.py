import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import args, consts, coeff
from questions.src.question.Types import Types, Complexity
from questions.src.question.utils.Utility import get_two_distinct


class Question69(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Moderate
        self.arg = random.choice(args)
        self.num = random.choice([8,9,10,11,12,13,14,15])
        self.const = random.choice(consts)
        self.coeff1,self.coeff2 = get_two_distinct(coeff)
        self.res = self.coeff1 * self.num + self.coeff2 * self.num + self.const
        self.body = "Given {arg}={num} What is {coeff1}{arg} + {coeff2}{arg} + {const}?"\
            .format(coeff1=self.coeff1, coeff2=self.coeff2, arg=self.arg, num=self.num, const=self.const)

    def question(self):
        return self.body

    def answer(self):
        return "{0}".format(self.res)
