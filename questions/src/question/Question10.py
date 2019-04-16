import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import girls, items, simple_fractions
from .Types import Types, Complexity


class Question10(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_Got_Spent_Left
        self.complexity = Complexity.Basic
        self.subject = random.choice(girls)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.got = self.ratio.denominator*random.choice(range(2, 10))
        self.spent = self.got * self.ratio

        self.body = "{subj} has {got} pounds, she spends {ratio} on {item}. How much money she has spent?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, got=self.got)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} spent {spent} pounds".format(subj=self.subject, spent=self.spent)
