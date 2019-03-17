import random
from .Types import Types
from ..resources.Resource import boys, items, simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct


class Question13:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(3, 10))*spent_ratio.denominator
        self.spent = self.got*spent_ratio
        self.body = "{subj} spent {ratio1} of his money on {item1} and {ratio2} of his money on {item2}." \
                    "If he had {got} pounds, How much money has he spent?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    got=self.got)

    def question(self):
        return self.body

    def ask_user(self):
        return self.spent == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.spent}

    def answer(self):
        return "{subj} spent {spent}".format(subj=self.subject, spent=self.spent)

