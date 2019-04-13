import random

def get_n_distinct(elements, n):
    srand = random.SystemRandom()
    return sorted(srand.sample(elements, n))
    

def get_two_distinct(elements):
    return get_n_distinct(elements,2)

#this method will return 10, 5 when 5,10 is given
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

