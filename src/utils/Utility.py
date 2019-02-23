import random


def get_two_distinct(elements):
    srand = random.SystemRandom()
    return sorted(srand.sample(elements, 2))
