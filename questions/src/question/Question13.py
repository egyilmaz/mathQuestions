import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, simple_fractions
from .utils.Utility import get_two_distinct
from .Types import Types,Complexity


class Question13(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_Got_Spent_Left
        self.complexity = Complexity.Basic
        self.subject = random.choice(boys)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(2, 11))*self.ratio1.denominator*self.ratio2.denominator
        self.spent = self.got*spent_ratio
        self.body = "{subj} spent {ratio1} of his money on {item1} and {ratio2} of his money on {item2}." \
                    "If he had {got} pounds, How much money has he spent?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    got=self.got)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} spent {spent}".format(subj=self.subject, spent=self.spent)

