import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import girls, items, simple_fractions
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types,Complexity


class Question14(BaseQuestion):
    def __init__(self):
        self.type = Types.Money_Got_Spent_Left
        self.complexity = Complexity.Moderate
        self.subject = random.choice(girls)
        self.item1, self.item2 = get_two_distinct(items)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        spent_ratio = self.ratio1 + self.ratio2
        self.got = random.choice(range(2, 11))*self.ratio1.denominator*self.ratio2.denominator
        self.spent = self.got*spent_ratio
        self.body = "{subj} spent {ratio1} of her money on {item1} and {ratio2} of her money on {item2}." \
                    " If she had {got} pounds, How much money is she left with?"\
            .format(subj=self.subject, ratio1=self.ratio1, ratio2=self.ratio2, item1=self.item1, item2=self.item2,
                    got=self.got)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} is left with {left}".format(subj=self.subject, left=self.got-self.spent)
