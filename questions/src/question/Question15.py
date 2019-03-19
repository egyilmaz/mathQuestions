import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import boys, items, simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct


class Question15(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(3, 10))*spent_ratio.denominator
        self.spent = self.got*spent_ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} spent {ratio1} of his money on {item1} and {ratio2} of his money on {item2}." \
                    " If he had {got} pounds, How much money is he left with?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    got=self.got)

    def question(self):
        return self.body

    def ask_user(self):
        return self.remaining == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.remaining}

    def answer(self):
        return "{subj} has now {rem}".format(subj=self.subject, rem=self.remaining)
