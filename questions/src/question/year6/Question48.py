
import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity

class Question48(BaseQuestion):
    def __init__(self):
        self.type = Types.Power
        self.complexity = Complexity.Moderate
        self.char = random.choice(['x','y','z'])
        self.num = random.choice([2,3,4,5])
        self.res = self.num*self.num*self.num

    def question(self):
        return "Given   "

    def graphic(self):
        a = r'${0}^2$ = {1}, Find ${0}^3$'.format(self.char,self.num*self.num)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
