from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import random
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib

class Question39(BaseQuestion):

    def __init__(self):
        self.type = Types.simplify_power
        self.complexity = Complexity.Moderate
        f = random.sample([6,7,8,9],2)
        s = random.sample([2,3],2)
        a,b = f[0],f[1]
        c,p = s[0],s[1] 
        self.q = f"$(\\frac{{{a**p}}}{{{b**p}}})^\\frac{{{-c}}}{{{p}}}$"
        self.res = sym.nsimplify((a**p/b**p)**(-c/p), rational=False)

    def question(self):
        return "Simplfy as much as possible and leave it as a fraction "

    def graphic(self):
        return self.encode_graphics(self.q, 20)

    def answer(self):
        return "{res}".format(res=self.res)

