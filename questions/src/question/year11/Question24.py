from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import random
from sympy import nsimplify
import matplotlib.pyplot as plt
import matplotlib

class Question24(BaseQuestion):

    def __init__(self):
        self.type = Types.find_value
        self.complexity = Complexity.Moderate
        dep = random.sample(['y','t','q'],1)[0]
        coef = random.sample(['m','n','p'],1)[0]
        indep = random.sample(['x','k','i','j'],1)[0]
        const = random.sample(['a','b','c'],1)[0]

        dep_val = random.sample([8,12,14,15],1)[0]
        coef_val = random.sample([-3, -4, 3, 4, ],1)[0]
        const_val = random.sample([-3, -5, 3, 5, 2, 1],1)[0]
        self.q=f"Given {dep} = {coef} * {indep} + {const}, and {coef} = {coef_val}, {const} = {const_val}, {dep} = {dep_val} Find the value of {indep} "
        self.res = nsimplify((dep_val - const_val)/coef_val,rational=True)

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q, 10)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
