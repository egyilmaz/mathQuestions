import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, random_fractions
from .Types import Types, Complexity


class Question56(BaseQuestion):
    def __init__(self):
        self.type = Types.Money_Got_Spent_Left
        self.complexity = Complexity.Advanced
        self.subject = random.choice(boys)
        self.duration = random.choice([1,2,3,4,5,10,15,20])
        self.ratio1 = random.choice(random_fractions)
        self.pocket = random.choice(range(2,5))*self.ratio1.denominator
        self.saved = self.ratio1*self.pocket*self.duration*7
        self.spent = (1-self.ratio1)*self.pocket*self.duration*7
        self.body = "{subj} has decided to save {ratio1} of his pocket money every day for the next {dur} weeks." \
                    " If he had saved {saved} pounds, How much he spent throughout that period?"\
            .format(subj=self.subject, ratio1=self.ratio1, dur=self.duration, saved=self.saved)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has spent {spent}".format(subj=self.subject, spent=self.spent)
