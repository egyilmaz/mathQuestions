from django.http import HttpResponse
from django.template import loader
from .src.question.QuestionFactory import QuestionFactory, nof_registered_questions
from .src.question.Types import Output


def index(request, nof_questions):
    return index_start_end(request, nof_questions, 1, nof_registered_questions)

def index_start_from(request, nof_questions, start_from):
    return index_start_end(request, nof_questions, start_from, nof_registered_questions)

def index_start_end(request, nof_questions, start, end):
    qf = QuestionFactory(Output.ONLINE)
    result = qf.ask(nof_questions, start, end) #return list of questions
    template = loader.get_template("questions/questions.html")
    context = {"questions_list":result}
    return HttpResponse(template.render(context,request))

