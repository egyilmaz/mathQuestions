import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, random_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question37(BaseQuestion):
    def __init__(self):
        self.type = Types.Money_Got_Spent_Left
        self.complexity = Complexity.Advanced
        self.subject = random.choice(boys)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(random_fractions)
        self.got = random.choice(range(2, 11))*self.ratio1.denominator*self.ratio2.denominator
        self.body = "{subj} has {got} pounds. He spends {ratio1} of his money on {item1} and then spends {ratio2} of remaining money on {item2}." \
                    " How much money is he left with?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    got=self.got)
        self.res = self.got*(1-self.ratio1)*(1-self.ratio2)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has now {rem}".format(subj=self.subject, rem=self.res)
