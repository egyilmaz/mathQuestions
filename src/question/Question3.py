import random
from src.question.Types import Types
from src.utils.Utility import get_two_distinct
from src.resources.Resource import subjects, values, items, coeff


# Question type is Ax = y,
class Question3:
    def __init__(self):
        self.type = Types.FIRST_ORDER_2_UNKNOWN
        self.body = "{subj1} has {coeff} times more {item} than {subj2}. If their total {item} count is {total}."
        self.item = random.choice(items)
        self.subj1, self.subj2 = get_two_distinct(subjects)
        self.question_text = 'How many each has? {subj1},{subj2}: '.format(subj1=self.subj1, subj2=self.subj2)
        self.subj2_qty = random.choice(values)
        self.coeff = random.choice(coeff)
        self.subj1_qty = self.coeff * self.subj2_qty
        self.total = self.subj1_qty + self.subj2_qty

    def result(self):
        return {self.subj1: self.subj1_qty, self.subj2: self.subj2_qty}

    def answer(self):
        return "{subj1} has {subj1_qty} where {subj2} has {subj2_qty} {item}, hence your answer should have "\
               "been {subj1_qty},{subj2_qty}".format(subj1=self.subj1
                                                     , subj1_qty=self.subj1_qty
                                                     , subj2=self.subj2
                                                     , subj2_qty=self.subj2_qty
                                                     , item=self.item)

    def __str__(self):
        return self.body.format(subj1=self.subj1, coeff=self.coeff, item=self.item, subj2=self.subj2, total=self.total)
