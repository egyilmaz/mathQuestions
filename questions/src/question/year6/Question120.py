import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
from sympy import sieve


class Question120(BaseQuestion):
    def __init__(self):
        self.type = [Types.Prime_number, Types.sat_reasoning]
        self.complexity = Complexity.Moderate

        nth_primes = random.sample(range(2, 25), 3)
        primes=[]
        for i in nth_primes:
            primes.append(sieve[i])
        others = random.sample([4,6,8,10,12,15,27,28,32,42,51,55,75,77,78,99], 5)
        bunch = primes+others
        random.shuffle(bunch)
        self.body = "Find the prime number within {0}".format(bunch)
        self.res="{0} are the primes".format(primes)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
