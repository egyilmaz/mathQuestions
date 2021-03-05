import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import girls, random_fractions
from questions.src.question.year6.Types import Types, Complexity


class Question55(BaseQuestion):
    def __init__(self):
        self.type = Types.Money_Got_Spent_Left
        self.complexity = Complexity.Moderate
        self.subject = random.choice(girls)
        self.duration = random.choice([1,2,3,4,5,10,15,20])
        self.ratio1 = random.choice(random_fractions)
        self.pocket = random.choice(range(2,5))*self.ratio1.denominator
        self.saved = self.ratio1*self.pocket*self.duration*7
        self.body = "{subj} has decided to save {ratio1} of her pocket money every day for the next {dur} weeks." \
                    " If she had saved {saved} pounds, How much pocket money is she given everyday?"\
            .format(subj=self.subject, ratio1=self.ratio1, dur=self.duration, saved=self.saved)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} is given {given}".format(subj=self.subject, given=self.pocket)
