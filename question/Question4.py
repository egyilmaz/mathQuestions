import random


# Question type is Ax = B,
class Question4:
    args = ['X', 'Y', 'A', 'B', 'C']
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 60, 70, 80, 90]
    coeff = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__( self):
        self.body = "Given {coeff}{arg} = {result}."
        self.arg = random.choice(Question4.args)
        self.coeff = random.choice(Question4.coeff)
        self.val = random.choice(Question4.vals)
        self.result = self.coeff * self.val

    def ask(self):
        user_input = input("What is {arg}: ".format(arg=self.arg))
        return int(user_input) == self.val

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, result=self.result)
