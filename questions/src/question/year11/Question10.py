from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question10(BaseQuestion):

    def __init__(self):
        self.type = Types.square_diff
        self.complexity = Complexity.Moderate
        cand = [1,2,3,4,5,6,7,8,9]
        a = random.sample(cand,1)[0]
        b = random.sample([2,3,4],1)[0]
        #the form is a* (x^2 -b^2)
        last = a*b*b       
        self.res =  solve([Eq(a*(x**2 - b**2), 0)])
        if a == 1:
            a = ""
        self.q = f'${a}x^2 -{last}$'
        
    def question(self):
        return "Factorise "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


