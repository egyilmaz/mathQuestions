from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from sympy import expand,symbols
from sympy.abc import x, y
import random

class Question8(BaseQuestion):

    def __init__(self):
        self.type = Types.expand_triple
        self.complexity = Complexity.Moderate
        cand = [-6,-5,-4,-3,-2,2,3,4,5,6]
        a = random.sample(cand,1)[0]
        b = random.sample(cand,1)[0]
        c = random.sample(cand,1)[0]
        d = random.sample(cand,1)[0]
        e = random.sample(cand,1)[0]
        f = random.sample(cand,1)[0]

        first = b
        if first > 0:
            first = f"+{first}"

        second = d
        if second > 0:
            second = f"+{second}"        

        third = f
        if third > 0:
            third = f"+{third}"        

        self.q = f'$({a}x {first})({c}x {second})({e}x {third})$'
        self.res = f'${a*c*e}x^3+{a*d*e+b*c*e+a*c*f}x^2 +{b*d*e+a*d*f+b*c*f}x +{b*d*f}$'
        #self.res2 = expand((a*x+b)*(c*x+d)*(e*x+f))

    def question(self):
        return "Expand then simplfy  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return f"Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


