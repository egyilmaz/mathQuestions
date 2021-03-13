from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random

class Question14(BaseQuestion):

    q = [(2,3),(3,3),(5,2),(7,2)]

    def __init__(self):
        self.type = Types.power
        self.complexity = Complexity.Basic
        nums = random.sample(Question14.q, 2)
        power = random.choice([2,3,4,5])
        self.q=r'$({v1}^{p1}x{v2}^{p2})^{p3}$'.format(v1=nums[0][0],p1=nums[0][1],v2=nums[1][0],p2=nums[1][1],p3=power)
        self.a=r'${v1}^{{{p1}}}x{v2}^{{{p2}}}$'.format(v1=nums[0][0],p1=nums[0][1]*power,v2=nums[1][0],p2=nums[1][1]*power)\
                 + f' or {((nums[0][0]**nums[0][1]) * (nums[1][0]**nums[1][1]))**power}'
    def question(self):
        return "Evaluate (do not calculate)"

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)

