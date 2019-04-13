import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import girls, items, simple_fractions


class Question12(BaseQuestion):
    def __init__(self):
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

    def answer(self):
        return "{subj} spent {spent}".format(subj=self.subject, spent=self.spent)
