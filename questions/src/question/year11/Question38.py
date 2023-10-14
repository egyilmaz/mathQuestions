from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import random
from sympy import nsimplify
import matplotlib.pyplot as plt
import matplotlib

class Question38(BaseQuestion):

    def __init__(self):
        self.type = Types.repeating
        self.complexity = Complexity.Complex
        whole = random.sample([1,2,3,4,5,6],1)[0]
        rep = random.sample([2,3,4,5,6],1)[0]
        self.q=f"Write down the steps to represent ${whole}.\overline{{{rep}}}$ as $\dfrac{{{whole*9+rep}}}{{9}}$"
        self.res = f"Write the ${whole}.\overline{{{rep}}}$ as ${whole} + 0.\overline{{{rep}}}$. Write $x=0.\overline{{{rep}}}$ "\
                   f"which is equivalent to x=0.{rep}{rep}{rep}... then multiply each side by 10 to get 10x={rep}.{rep}{rep}{rep}..."\
                   f"Write the repeated part as $10x = {rep}.\overline{{{rep}}}$ Then rewrite it as $10x = {rep} + 0.\overline{{{rep}}}$"\
                   f"Which boils down to 10x = {rep} + x, and then x = $\dfrac{{{rep}}}{{9}}$ and whole thing becomes ${whole}+\dfrac{{{rep}}}{{9}}$"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q, 10)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
