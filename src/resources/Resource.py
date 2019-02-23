subjects = ["George", "Dragon", "Emily", "Stuart"]
items = ["marbles", "pens", "pencils"]
args = ['X', 'Y', 'A', 'B', 'C']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 60, 70, 80, 90]
coeff = [2, 3, 4, 5, 10, 100]
consts = [5, 10, 15, 20, 25]


def get_user_input_2arg(subj1, subj2):
    try:
        user_input = input('How many each has {subj1},{subj2}: '.format(subj1=subj1, subj2=subj2))
        first, second = user_input.split(",")
        return int(first), int(second)
    except ValueError:
        print('Integer input expected')
        return 0, 0


def get_user_input(subj1):
    try:
        user_input = input("What is {arg}: ".format(arg=subj1))
        return int(user_input)
    except ValueError:
        print('Integer input expected')
        return 0

