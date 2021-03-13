from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random
import math

def get_pfac(number):
        prime_factors = []
        while number % 2 == 0:
            prime_factors.append(2)
            number = number / 2
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                prime_factors.append(int(i))
                number = number / i
        if number > 2:
            prime_factors.append(int(number))
        return prime_factors


class Question3(BaseQuestion):

    q = [2, 10, 18, 21, 25, 19, 24, 32, 28, 46, 125, 1000, 100, 256, 128, 64, 84, 81, 39, 150, 300]

    def __init__(self):
        self.type = Types.prime_factors
        self.complexity = Complexity.Basic
        facs = random.sample(Question3.q, 4)
        self.q = f"What are the prime factorizations of the following numbers  {' , '.join([str(i) for i in facs])}"
        res = []
        for fac in facs:
            pfacs = get_pfac(fac)
            res.append('x'.join([str(i) for i in pfacs]))
        self.r = ' , '.join(res)

    def question(self):
        return f"{self.q}"

    def answer(self):
        return f"{self.r}"

