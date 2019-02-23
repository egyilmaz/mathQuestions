import random


# Question type is Ax + B = C,
class Question5:
    args = ['X', 'Y', 'A', 'B', 'C']
    consts = [5, 10, 15, 20, 25]
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 60, 70, 80, 90]
    coeff = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__( self):
        self.body = "Given {coeff}{arg} + {const} = {result}."
        self.arg = random.choice(Question5.args)
        self.const = random.choice(Question5.consts)
        self.coeff = random.choice(Question5.coeff)
        self.val = random.choice(Question5.vals)
        self.result = self.coeff * self.val + self.const

    def ask(self):
        user_input = input("What is {arg}: ".format(arg=self.arg))
        return int(user_input) == self.val

    def answer(self):
        return "{arg} is {value}".format(arg=self.arg, value=self.val)

    def __str__(self):
        return self.body.format(coeff=self.coeff, arg=self.arg, result=self.result, const = self.const)
