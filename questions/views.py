from django.http import HttpResponse
from django.template import loader
from questions.src.question.QuestionFactory import QuestionFactory, nof_registered_questions

MAX_ALLOWED_QUESTIONS = 100


def index(request, nof_questions):
    return index_start_end(request, nof_questions, 1, nof_registered_questions)


def index_start_from(request, nof_questions, start_from):
    return index_start_end(request, nof_questions, start_from, nof_registered_questions)


def get_question_list(nof_questions, start, end):
    nof_questions = min(nof_questions, MAX_ALLOWED_QUESTIONS) # here is our bottleneck.
    qf = QuestionFactory()
    return qf.ask_question(nof_questions, start, end) #return list of questions


def index_start_end(request, nof_questions, start, end):
    questions = get_question_list(nof_questions, start, end)
    result=[]
    for q in questions:
        result.append((q.question(),q.graphic()))
    template = loader.get_template("questions/questions.html")
    context = {"questions_list":result}
    return HttpResponse(template.render(context,request))


#----------------------------------------------------------------------------------------
# Questions and answers API

def render_qa(request, questions):
    result=[]
    qid=0
    for q in questions:
        result.append((qid,q.question(),q.graphic(),q.meta(),q.answer()))
        qid = qid + 1
    template = loader.get_template("questions/qa.html")
    context = {"questions_list":result}
    return HttpResponse(template.render(context,request))


def questions_answers(request, nof_questions):
    questions = get_question_list(nof_questions, 1, nof_registered_questions)
    return render_qa(request, questions)

#----------------------------------------------------------------------------------------------
# Filtering questions by their type and complexity.


def qa_stats(request):
    qf = QuestionFactory()
    return HttpResponse( qf.statistics() )


def qa_by_type(request, qtype, nof_questions):
    return qa_by_type_complexity(request, qtype, None, nof_questions)


def qa_by_complexity(request, complexity, nof_questions):
    return qa_by_type_complexity(request, None, complexity, nof_questions)


def qa_by_type_complexity(request, qtype, complexity, nof_questions):
    nof_questions = min(nof_questions, MAX_ALLOWED_QUESTIONS) # here is our bottleneck.
    qf = QuestionFactory()
    questions = qf.ask_filtered(nof_questions, qtype, complexity)
    return render_qa(request, questions)
