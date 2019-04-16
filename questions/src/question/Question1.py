import random
from .BaseQuestion import BaseQuestion
from .utils.Utility import get_two_distinct
from .resources.Resource import subjects, values, items
from .Types import Types, Complexity


# Question type is x + N = y, worded as, y has N many more items then x.
class Question1(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Basic
        self.subj1, self.subj2 = get_two_distinct(subjects)
        self.subj1_qty, self.subj2_qty = get_two_distinct(values)
        self.item = random.choice(items)
        self.diff = self.subj2_qty - self.subj1_qty
        self.total = self.subj1_qty + self.subj2_qty
        self.body = "{subj2} has {qty} many more {item} then {subj1}, If they have {total} {item} in total."\
            .format(subj1=self.subj1, qty=self.diff, item=self.item, subj2=self.subj2, total=self.total)
        self.question_text = 'How many each has? {subj1},{subj2}: '.format(subj1=self.subj1, subj2=self.subj2)

    def question(self):
        return self.body + ' ' + self.question_text

    def answer(self):
        return "{subj1} has {subj1_qty} where {subj2} has {subj2_qty} {item}, hence your answer should have " \
               "been {subj1_qty},{subj2_qty}".format(subj1=self.subj1, subj1_qty=self.subj1_qty, subj2=self.subj2
                                                     , subj2_qty=self.subj2_qty, item=self.item)

