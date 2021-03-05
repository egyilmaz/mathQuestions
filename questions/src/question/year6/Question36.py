import random
from fractions import Fraction
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question36(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_simplify
        self.complexity = Complexity.Moderate
        self.num = random.choice(range(2, 11)) * random.choice([3,5,6,8,9,12]) * random.choice([5,6,7,8,9])
        self.denum = random.choice(range(8, 13)) * random.choice([2,3,5,6,8,9,12]) * random.choice([5,6,7,8,9,10])
        self.res = Fraction(self.num, self.denum)

    def question(self):
        return "Simplify "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$' \
            .format(self.num, self.denum)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is"

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$'.format(self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)
