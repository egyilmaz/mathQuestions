import random
from src.question.Types import Types
from src.resources.Resource import boys, items, simple_fractions
from src.utils.Utility import ask_interactive_1arg, get_two_distinct


class Question17:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        if self.ratio2 > self.ratio1:
            self.ratio1, self.ratio2 = self.ratio2, self.ratio1
        self.res = self.ratio1 - self.ratio2
        self.body = "{ratio1} - {ratio2} = ?".format(ratio1=self.ratio1, ratio2=self.ratio2)

    def question(self):
        return self.body

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.res}

    def answer(self):
        return "{res}".format(res=self.res)

