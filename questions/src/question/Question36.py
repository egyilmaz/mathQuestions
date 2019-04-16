import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, random_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question36(BaseQuestion):
    def __init__(self):
        self.type = Types.Money_Got_Spent_Left
        self.complexity = Complexity.Advanced
        self.subject = random.choice(boys)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(random_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(2, 11))*spent_ratio.denominator #using spent_ratio will make it harder to compute
        self.spent = self.got*spent_ratio
        self.remaining = self.got - self.spent
        self.body = "{subj} spent {ratio1} of his money on {item1} and {ratio2} of his money on {item2}." \
                    " If he had {spent} pounds, How much money is he left with?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    spent=self.spent)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has now {rem}".format(subj=self.subject, rem=self.remaining)
