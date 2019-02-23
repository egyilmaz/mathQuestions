import random
from src.utils.Utility import get_two_distinct
from src.resources.Resource import subjects, values, items


# Question type is x - N = y, worded as, y has N less items then x.
class Question2:
    def __init__(self, user_input):
        self.user_input = user_input
        self.body = "{subj1} has {qty} less {item} then {subj2}, If they have {total} {item} in total."
        self.subj1, self.subj2 = get_two_distinct(subjects)
        self.subj1_qty, self.subj2_qty = get_two_distinct(values)
        self.item = random.choice(items)
        self.diff = self.subj2_qty - self.subj1_qty
        self.total = self.subj1_qty + self.subj2_qty

    def ask(self):
        first, second = self.user_input(self.subj1, self.subj2)
        return self.__eval__(first, second)

    def answer(self):
        return "{subj1} has {subj1_qty} where {subj2} has {subj2_qty} {item}, hence your answer should have"\
               " been {subj1_qty},{subj2_qty}".format(subj1=self.subj1
                                                      , subj1_qty=self.subj1_qty
                                                      , subj2=self.subj2
                                                      , subj2_qty=self.subj2_qty
                                                      , item=self.item)

    def __str__(self):
        return self.body.format(subj1=self.subj1, qty=self.diff, item=self.item, subj2=self.subj2, total=self.total)

    def __eval__(self, subj1, subj2):
        return subj1 == self.subj1_qty and subj2 == self.subj2_qty
