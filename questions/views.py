from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import Template, RequestContext
from questions.src.question.QuestionFactory import QuestionFactory, nof_registered_questions
from django.contrib.auth import authenticate, login

MAX_ALLOWED_QUESTIONS = 100

def qa_stats(request):
    qf = QuestionFactory()
    return HttpResponse( qf.statistics(True,True) )

def qa_stats_by_type(request):
    qf = QuestionFactory()
    return HttpResponse( qf.statistics(True, False) )

def qa_stats_by_complexity(request):
    qf = QuestionFactory()
    return HttpResponse( qf.statistics(False, True) )

def qa_index_start_from(request, nof_questions, start_from):
    return qa_index_start_end(request, nof_questions, start_from, nof_registered_questions)

def qa_index_start_end(request, nof_questions, start, end):
    questions = get_question_list(nof_questions, start, end)
    return render_qa(request, questions)

def qa_questions_answers(request, nof_questions):
    questions = get_question_list(nof_questions, 1, nof_registered_questions)
    return render_qa(request, questions)

def qa_by_type(request, qtype, nof_questions):
    return qa_by_type_complexity(request, qtype, None, nof_questions)

def qa_by_complexity(request, complexity, nof_questions):
    return qa_by_type_complexity(request, None, complexity, nof_questions)

def qa_by_type_complexity(request, qtype, complexity, nof_questions):
    nof_questions = min(nof_questions, MAX_ALLOWED_QUESTIONS) # here is our bottleneck.
    qf = QuestionFactory()
    questions = qf.ask_filtered(nof_questions, qtype, complexity)
    return render_qa(request, questions)

def get_question_list(nof_questions, start, end):
    nof_questions = min(nof_questions, MAX_ALLOWED_QUESTIONS) # here is our bottleneck.
    qf = QuestionFactory()
    return qf.ask_question(nof_questions, start, end) #return list of questions

def render_qa(request, questions):
    header_str = "<!DOCTYPE html>"\
                "<title> Review Your Maths </title>"\
                "<head>"\
                    "{% load static %}"\
                    "<link rel=\"stylesheet\" href=\"{% static 'questions/css/the.css' %}\">"\
                    "<script src=\"{% static 'questions/js/eval_and_submit.js'%}\"></script>"\
                "</head>"
    hdr_template = Template(header_str)
    response = hdr_template.render(RequestContext(request,{}))
    response += "<body><ol>"
    qid=0
    for q in questions:
        response+="<li>"
        template = q.template()
        context = q.context()
        context.update({"qid":qid})
        c = RequestContext(request, context)
        response += template.render(c)
        qid += 1
        response += "</li>"
    response += "</ol></body>"
    return HttpResponse(response)


def qa_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'questions/login_error.html')
    else:
        return HttpResponseNotAllowed()

