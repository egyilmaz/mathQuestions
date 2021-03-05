import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity

class Question52(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_Second_order_one_unknown
        self.complexity = Complexity.Moderate
        self.var1 = random.choice(['x','y','z'])
        self.num1 = random.choice([2,3,4,5])
        self.asked = self.num1*self.num1 + self.num1*self.num1

    def question(self):
        return "Given "

    def graphic(self):
        a = r'${var1}^2$ + ${var1}^2$ = {asked}, What is {var1} ?'.format(var1=self.var1,asked=self.asked)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.num1)
