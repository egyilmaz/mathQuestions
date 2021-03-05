import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity

class Question49(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_Second_order_one_unknown
        self.complexity = Complexity.Basic
        self.char = random.choice(['x','y','z'])
        self.num = random.choice([2,3,4,5])
        self.res = self.num*self.num + 2*self.num + 1

    def question(self):
        return "Given   "

    def graphic(self):
        a = r'{0} = {1}, Find ${0}^2+2{0}+1$'.format(self.char,self.num)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
