from question.QuestionFactory import QuestionFactory

if __name__ == '__main__':
    qf = QuestionFactory()
    while(True):
        for i in range(5):
            qf.ask(i)

