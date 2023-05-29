def get_nof_questions():
    return 20

def get_question(qtype):
    if qtype == 0:
        from questions.src.question.year9.Question1 import Question1
        return Question1()
    if qtype == 1:
        from questions.src.question.year9.Question2 import Question2
        return Question2()
    if qtype == 2:
        from questions.src.question.year9.Question3 import Question3
        return Question3()
    if qtype == 3:
        from questions.src.question.year9.Question4 import Question4
        return Question4()
    if qtype == 4:
        from questions.src.question.year9.Question5 import Question5
        return Question5()
    if qtype == 5:
        from questions.src.question.year9.Question6 import Question6
        return Question6()
    if qtype == 6:
        from questions.src.question.year9.Question7 import Question7
        return Question7()
    if qtype == 7:
        from questions.src.question.year9.Question8 import Question8
        return Question8()
    if qtype == 8:
        from questions.src.question.year9.Question9 import Question9
        return Question9()
    if qtype == 9:
        from questions.src.question.year9.Question10 import Question10
        return Question10()
    if qtype == 10:
        from questions.src.question.year9.Question11 import Question11
        return Question11()
    if qtype == 11:
        from questions.src.question.year9.Question12 import Question12
        return Question12()
    if qtype == 12:
        from questions.src.question.year9.Question13 import Question13
        return Question13()
    if qtype == 13:
        from questions.src.question.year9.Question14 import Question14
        return Question14()
    if qtype == 14:
        from questions.src.question.year9.Question15 import Question15
        return Question15()
    if qtype == 15:
        from questions.src.question.year9.Question16 import Question16
        return Question16()
    if qtype == 16:
        from questions.src.question.year9.Question17 import Question17
        return Question17()
    if qtype == 17:
        from questions.src.question.year9.Question18 import Question18
        return Question18()
    if qtype == 18:
        from questions.src.question.year9.Question19 import Question19
        return Question19()
    if qtype == 19:
        from questions.src.question.year9.Question20 import Question20
        return Question20()
    
