from src.question.QuestionFactory import QuestionFactory
from src.question.Types import Output

if __name__ == '__main__':
    qf = QuestionFactory(Output.ONLINE)
    for i in range(1, 2):
        qf.ask()

