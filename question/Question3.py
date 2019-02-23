import random
from utils.Utility import get_two_distinct


# Question type is Ax = y,
class Question3:
    subjects = ["George", "Dragon", "Emily", "Stuart"]
    items = ["marbles", "pens", "pencils"]
    qty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    coeff = [2, 3, 4, 5, 10, 100]

    def __init__( self):
        self.body = "{subj1} has {coeff} times more {item} than {subj2}. If their total {item} count is {total}."
        self.item = random.choice(Question3.items)
        self.subj1, self.subj2 = get_two_distinct(Question3.subjects)
        self.subj2_qty = random.choice(Question3.qty)
        self.coeff = random.choice(Question3.coeff)
        self.subj1_qty =  self.coeff * self.subj2_qty
        self.total = self.subj1_qty + self.subj2_qty

    def ask(self):
        user_input = input("How many each has {subj1},{subj2}: ".format(subj1=self.subj1,subj2=self.subj2))
        subj1, subj2 = user_input.split(",")
        return self.__eval__(int(subj1), int(subj2))

    def answer(self):
        return "{subj1} has {subj1_qty} where {subj2} has {subj2_qty} {item}, hence your answer should have been {subj1_qty},{subj2_qty}".format(subj1=self.subj1, subj1_qty=self.subj1_qty, subj2=self.subj2, subj2_qty=self.subj2_qty, item=self.item)

    def __str__(self):
        return self.body.format(subj1=self.subj1, coeff=self.coeff, item=self.item, subj2=self.subj2, total=self.total)

    def __eval__(self, subj1, subj2):
        return subj1 == self.subj1_qty and subj2 == self.subj2_qty
