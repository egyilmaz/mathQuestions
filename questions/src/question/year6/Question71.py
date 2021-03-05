import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import args
from questions.src.question.year6.Types import Types, Complexity
from questions.src.question.utils.Utility import get_n_distinct

class Question71(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Advanced
        self.arg1,self.arg2,self.arg3 = get_n_distinct(args,3)
        self.num1,self.num2,self.num3 = get_n_distinct(range(20,50),3)
        self.const = random.choice(range(10,20))
        self.num1 = self.num2 + self.num3 - self.const
        self.body = "Given {arg1} = {arg2} + {arg3} - {const}. If {arg1}={num1} and {arg2}={num2}, What is {arg3}?"\
            .format(arg1=self.arg1, arg2=self.arg2, arg3=self.arg3, num1=self.num1, num2=self.num2, const=self.const)

    def question(self):
        return self.body

    def answer(self):
        return "{0}".format(self.num3)
