from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity

def cube(num):
    return num*num*num

class Question24(BaseQuestion):
    def __init__(self):
        self.type = Types.Power
        self.complexity = Complexity.Moderate
        self.first, self.second, self.third, self.fourth = get_n_distinct(range(0,11),4)
        self.res = [cube(self.first),cube(self.second),cube(self.third),cube(self.fourth)]

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0}^3, {1}^3, {2}^3, {3}^3$'.format(self.first,self.second,self.third,self.fourth)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
