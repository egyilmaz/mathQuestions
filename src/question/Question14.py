import random
from src.question.Types import Types
from src.resources.Resource import girls, items, simple_fractions
from src.utils.Utility import ask_interactive_1arg, get_two_distinct


class Question14:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(girls)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(3, 10))*spent_ratio.denominator
        self.spent = self.got*spent_ratio
        self.body = "{subj} spent {ratio1} of her money on {item1} and {ratio2} of her money on {item2}." \
                    " If she had spent {spent} pounds, How much money she had?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    spent=self.spent)

    def question(self):
        return self.body

    def ask_user(self):
        return self.got == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.got}

    def answer(self):
        return "{subj} had {got}".format(subj=self.subject, got=self.got)
