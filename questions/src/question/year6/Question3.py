import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.resources.Resource import subjects, values, items, coeff
from questions.src.question.Types import Types, Complexity


# Question type is Ax = y,
class Question3(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Moderate
        self.item = random.choice(items)
        self.subj1, self.subj2 = get_two_distinct(subjects)
        self.subj2_qty = random.choice(values)
        self.coeff = random.choice(coeff)
        self.subj1_qty = self.coeff * self.subj2_qty
        self.total = self.subj1_qty + self.subj2_qty
        self.body = "{subj1} has {coeff} times more {item} than {subj2}. If their total {item} count is {total}."\
            .format(subj1=self.subj1, coeff=self.coeff, item=self.item, subj2=self.subj2, total=self.total)
        self.question_text = 'How many each has? {subj1},{subj2}: '.format(subj1=self.subj1, subj2=self.subj2)

    def question(self):
        return self.body + ' ' + self.question_text

    def answer(self):
        return "{subj1} has {subj1_qty} where {subj2} has {subj2_qty} {item}, hence your answer should have "\
               "been {subj1_qty},{subj2_qty}".format(subj1=self.subj1, subj1_qty=self.subj1_qty, subj2=self.subj2
                                                     , subj2_qty=self.subj2_qty, item=self.item)