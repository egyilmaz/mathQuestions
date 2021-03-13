from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random

class Question15(BaseQuestion):

    q = [(2,3),(2,3),(3,5),(3,4),(4,5),(5,2),(7,2),('t',2),('a','b'),('3','y')]

    def __init__(self):
        self.type = Types.power
        self.complexity = Complexity.Basic
        nums = random.choice(Question15.q)
        power = random.choice([2,3,4,5])
        self.q=r'$({v1}*{v2})^{p1}$'.format(v1=nums[0],v2=nums[1],p1=power)
        self.a=r'${v1}^{{{p1}}}*{v2}^{{{p1}}}$'.format(v1=nums[0],v2=nums[1],p1=power)
    def question(self):
        return "Evaluate (do not calculate)"

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)

