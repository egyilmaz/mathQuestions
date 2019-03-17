import random
from .Types import Types
from ..resources.Resource import girls, items, pound, pence, simple_fractions
from ..utils.Utility import ask_interactive_1arg


class Question10:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(girls)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.got = self.ratio.denominator*random.choice(range(2, 10))
        self.spent = self.got * self.ratio

        self.body = "{subj} has {got} pounds, she spends {ratio} on {item}. How much money she has spent?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, got=self.got)

    def question(self):
        return self.body

    def ask_user(self):
        return self.spent == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.spent}

    def answer(self):
        return "{subj} spent {spent} pounds".format(subj=self.subject, spent=self.spent)
