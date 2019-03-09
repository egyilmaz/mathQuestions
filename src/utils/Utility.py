import random


def get_two_distinct(elements):
    srand = random.SystemRandom()
    return sorted(srand.sample(elements, 2))


def descending(first, second):
    if second > first:
        return second, first
    else:
        return first, second

def ask_interactive_2arg(question_text):
    try:
        user_input = input(question_text)
        first, second = user_input.split(",")
        return int(first), int(second)
    except ValueError:
        print('Integer input expected')
        return 0, 0


def ask_interactive_1arg(question_text):
    try:
        user_input = input(question_text)
        return int(user_input)
    except ValueError:
        print('Integer input expected')
        return 0

