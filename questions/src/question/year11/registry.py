def get_nof_questions():
    return 24

def get_question(qtype):
    if qtype == 0:
        from questions.src.question.year11.Question1 import Question1
        return Question1()
    if qtype == 1:
        from questions.src.question.year11.Question2 import Question2
        return Question2()
    if qtype == 2:
        from questions.src.question.year11.Question3 import Question3
        return Question3()
    if qtype == 3:
        from questions.src.question.year11.Question4 import Question4
        return Question4()
    if qtype == 4:
        from questions.src.question.year11.Question5 import Question5
        return Question5()
    if qtype == 5:
        from questions.src.question.year11.Question6 import Question6
        return Question6()
    if qtype == 6:
        from questions.src.question.year11.Question7 import Question7
        return Question7()
    if qtype == 7:
        from questions.src.question.year11.Question8 import Question8
        return Question8()
    if qtype == 8:
        from questions.src.question.year11.Question9 import Question9
        return Question9()
    if qtype == 9:
        from questions.src.question.year11.Question10 import Question10
        return Question10()
    if qtype == 10:
        from questions.src.question.year11.Question11 import Question11
        return Question11()
    if qtype == 11:
        from questions.src.question.year11.Question12 import Question12
        return Question12()
    if qtype == 12:
        from questions.src.question.year11.Question13 import Question13
        return Question13()
    if qtype == 13:
        from questions.src.question.year11.Question14 import Question14
        return Question14()
    if qtype == 14:
        from questions.src.question.year11.Question15 import Question15
        return Question15()
    if qtype == 15:
        from questions.src.question.year11.Question16 import Question16
        return Question16()
    if qtype == 16:
        from questions.src.question.year11.Question17 import Question17
        return Question17()
    if qtype == 17:
        from questions.src.question.year11.Question18 import Question18
        return Question18()
    if qtype == 18:
        from questions.src.question.year11.Question19 import Question19
        return Question19()
    if qtype == 19:
        from questions.src.question.year11.Question20 import Question20
        return Question20()    
    if qtype == 20:
        from questions.src.question.year11.Question21 import Question21
        return Question21()
    if qtype == 21:
        from questions.src.question.year11.Question22 import Question22
        return Question22()
    if qtype == 22:
        from questions.src.question.year11.Question23 import Question23
        return Question23()
    if qtype == 23:
        from questions.src.question.year11.Question24 import Question24
        return Question24()
