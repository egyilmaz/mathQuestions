import random
from src.question.Types import Types
from src.resources.Resource import boys, items, pound, simple_fractions
from src.utils.Utility import ask_interactive_1arg


class Question11:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.spent = random.choice(pound)
        self.got = self.spent / self.ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} has {got} pounds, he spends {ratio} on {item}. How much money he has left?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, got=self.got)

    def question(self):
        return self.body

    def ask_user(self):
        return self.remaining == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.remaining}

    def answer(self):
        return "{subj} has {rem} pounds left".format(subj=self.subject, rem=self.remaining)
