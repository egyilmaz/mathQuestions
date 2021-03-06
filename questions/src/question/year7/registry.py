def get_nof_questions():
    return 6

def get_question(qtype):
    if qtype == 0:
        from questions.src.question.year7.Question1 import Question1
        return Question1()

    if qtype == 1:
        from questions.src.question.year7.Question2 import Question2
        return Question2()

    if qtype == 2:
        from questions.src.question.year7.Question3 import Question3
        return Question3()

    if qtype == 3:
        from questions.src.question.year7.Question4 import Question4
        return Question4()

    if qtype == 4:
        from questions.src.question.year7.Question5 import Question5
        return Question5()

    if qtype == 5:
        from questions.src.question.year7.Question6 import Question6
        return Question6()
