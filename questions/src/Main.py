from QuestionFactory import QuestionFactory
from question.Types import Output

if __name__ == '__main__':
    qf = QuestionFactory(Output.PRINTED)
    nof_pages = input('How many pages ?')
    nof_question_per_page = input('How many questions per page?')
    for i in range(1, int(nof_pages)+1):
        qf.ask(int(nof_question_per_page))

