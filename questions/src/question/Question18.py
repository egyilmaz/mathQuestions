import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import args, consts, coeff, values
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


# Question type is Ax + B + Cx + D = E,
class Question18(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Moderate
        self.arg = random.choice(args)
        self.const1, self.const2 = get_two_distinct(consts)
        self.coeff1, self.coeff2 = get_two_distinct(coeff)
        self.val = random.choice(values)
        self.res = self.coeff1 * self.val + self.coeff2 * self.val + self.const1 + self.const2
        self.body = "Given {coeff1}{arg} + {const1} + {coeff2}{arg} + {const2} = {res}."\
            .format(coeff1=self.coeff1, arg=self.arg, res=self.res, const1=self.const1,
                    coeff2=self.coeff2, const2=self.const2)
        self.question_text = "What is {arg} ?".format(arg=self.arg)

    def question(self):
        return self.body + ' ' + self.question_text

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)
