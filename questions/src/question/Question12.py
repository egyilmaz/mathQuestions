import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import girls, items, pound, simple_fractions
from ..utils.Utility import ask_interactive_1arg


class Question12(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(girls)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.got = self.ratio.denominator*random.choice(range(2, 10))
        self.spent = self.got * self.ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} spent {ratio} of her money on {item} and left with {rem}. How much money has she spent?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, rem=self.remaining)

    def question(self):
        return self.body

    def ask_user(self):
        return self.spent == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.spent}

    def answer(self):
        return "{subj} spent {spent}".format(subj=self.subject, spent=self.spent)
