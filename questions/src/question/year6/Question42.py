import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import boys, items, random_fractions
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types, Complexity


class Question42(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_add
        self.complexity = Complexity.Moderate
        self.num = random.choice([11,17,19,23,37])
        self.denum = random.choice([3,4,5,6,7])
        self.whole = int(self.num/self.denum)
        self.rem = self.num % self.denum

    def question(self):
        return "Represent the improper fraction "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$ as mixed number'.format(self.num, self.denum)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is"

    def answer_graphic(self):
        a = r'${0}\dfrac{{{1}}}{{{2}}}$'.format(self.whole, self.rem, self.denum)
        return self.encode_graphics(a)
