import random


def get_two_distinct(elements):
    srand = random.SystemRandom()
    return sorted(srand.sample(elements, 2))


def ask_interactive_2arg(question_text, subj1, subj2):
    try:
        user_input = input(question_text.format(subj1=subj1, subj2=subj2))
        first, second = user_input.split(",")
        return int(first), int(second)
    except ValueError:
        print('Integer input expected')
        return 0, 0


def ask_interactive_1arg(question_text, subj1):
    try:
        user_input = input(question_text.format(arg=subj1))
        return int(user_input)
    except ValueError:
        print('Integer input expected')
        return 0

