from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity

def sq(num):
    return num*num

class Question23(BaseQuestion):
    def __init__(self):
        self.type = Types.Power
        self.complexity = Complexity.Basic
        self.first, self.second, self.third, self.fourth = get_n_distinct(range(0,21),4)
        self.res = [sq(self.first),sq(self.second),sq(self.third),sq(self.fourth)]

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0}^2, {1}^2, {2}^2, {3}^2$'.format(self.first,self.second,self.third,self.fourth)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
