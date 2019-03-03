import random
from src.question.Types import Types
from src.resources.Resource import girls, items, pound, simple_fractions
from src.utils.Utility import ask_interactive_1arg


class Question12:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(girls)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.spent = random.choice(pound)
        self.got = self.spent / self.ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} spent {ratio} of her money on {item} and left with {rem}. How much money she has spent?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, rem=self.remaining)

    def question(self):
        return self.body

    def ask_user(self):
        return self.spent == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.spent}

    def answer(self):
        return "{subj} spent {spent}".format(subj=self.subject, spent=self.spent)
