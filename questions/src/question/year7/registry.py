def get_nof_questions():
    return 13

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

    if qtype == 6:
        from questions.src.question.year7.Question7 import Question7
        return Question7()

    if qtype == 7:
        from questions.src.question.year7.Question8 import Question8
        return Question8()

    if qtype == 8:
        from questions.src.question.year7.Question9 import Question9
        return Question9()

    if qtype == 9:
        from questions.src.question.year7.Question10 import Question10
        return Question10()

    if qtype == 10:
        from questions.src.question.year7.Question11 import Question11
        return Question11()

    if qtype == 11:
        from questions.src.question.year7.Question12 import Question12
        return Question12()

    if qtype == 12:
        from questions.src.question.year7.Question13 import Question13
        return Question13()
