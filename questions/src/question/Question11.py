import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, simple_fractions


class Question11(BaseQuestion):
    def __init__(self):
        self.subject = random.choice(boys)
        self.item = random.choice(items)
        self.ratio = random.choice(simple_fractions)
        self.got = self.ratio.denominator*random.choice(range(2, 10))
        self.spent = self.got * self.ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} has {got} pounds, he spends {ratio} on {item}. How much money he has left?"\
            .format(subj=self.subject, ratio=self.ratio, item=self.item, got=self.got)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has {rem} pounds left".format(subj=self.subject, rem=self.remaining)
