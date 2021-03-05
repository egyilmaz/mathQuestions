def get_nof_questions():
    return 1

def get_question(qtype):
    if qtype == 0:
        from questions.src.question.year7.Question1 import Question1
        return Question1()

