from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import random
from sympy import nsimplify
import matplotlib.pyplot as plt
import matplotlib

class Question23(BaseQuestion):

    def __init__(self):
        self.type = Types.find_value
        self.complexity = Complexity.Moderate
        dep = random.sample(['y','t','q'],1)[0]
        coef = random.sample(['m','n','p'],1)[0]
        indep = random.sample(['x','k','i','j'],1)[0]
        const = random.sample(['a','b','c'],1)[0]
        self.q=f" Make {indep} the subject of {dep} = {coef} * {indep} + {const}"
        num = f"{dep} - {const}"
        denum = f"{coef}" 
        self.res = f"{indep} = $\\frac{{{num}}}{{{denum}}}$"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q, 10)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
