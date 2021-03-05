import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import boys, simple_fractions
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity

class Question22(BaseQuestion):
    def __init__(self):
        self.type = [Types.Fraction_add, Types.sat_arithmetic]
        self.complexity = Complexity.Moderate
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.int1, self.int2 = get_two_distinct(range(1,7))
        self.whole = self.int1+self.int2
        self.res = self.ratio1 + self.ratio2
    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0} \dfrac{{{1}}}{{{2}}} + {3}\dfrac{{{4}}}{{{5}}}$'.format(self.int1,self.ratio1.numerator,self.ratio1.denominator,self.int2,self.ratio2.numerator,self.ratio2.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is"

    def answer_graphic(self):
        a = r'{0}$\dfrac{{{1}}}{{{2}}}$'.format(self.whole,self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)
