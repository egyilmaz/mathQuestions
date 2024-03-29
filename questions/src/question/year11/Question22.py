from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
from sympy import nsimplify

class Question22(BaseQuestion):

    def __init__(self):
        self.type = Types.simplify_power
        self.complexity = Complexity.Basic
        a = random.sample([2,3],1)[0]
        c = a
        e = a
        g = a
        b = random.sample([0,1,2,3,4,5,6,7,8],1)[0]
        f = random.sample([0,1,2,3,4,5,6,7,8],1)[0]
        d = random.sample([0,1,2,3,4,5,6,7,8],1)[0]
        h = random.sample([0,1,2,3,4,5,6,7,8],1)[0]
        num=f"{a}^{{{b}}} x {c}^{{{d}}}"
        denum=f"{e}^{{{f}}} x {g}^{{{h}}}"
        sol = nsimplify(((a**b)*(c**d)) / ((e**f)*(g**h)),rational=True)
        self.q = f"$\\frac{{{num}}}{{{denum}}}$"
        self.res = r'{r1}'.format(r1=sol)

    def question(self):
        return "Simplify  "

    def graphic(self):
        return self.encode_graphics(self.q, 20)

    def answer(self):
        return "{res}".format(res=self.res)

