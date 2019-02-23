from src.question.QuestionFactory import QuestionFactory

if __name__ == '__main__':
    qf = QuestionFactory()
    while True:
        for i in range(1, 6):
            qf.ask(i)

