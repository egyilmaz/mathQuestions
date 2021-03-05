from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import Template, RequestContext
from questions.src.question.QuestionFactory import QuestionFactory
from django.contrib.auth import authenticate, login

MAX_ALLOWED_QUESTIONS = 200
qf = QuestionFactory()


def req_qa_stats(request, year):
    return HttpResponse( qf.statistics(True,True, year) )

def req_qa_stats_by_type(request, year):
    return HttpResponse( qf.statistics(True, False, year) )

def req_qa_stats_by_complexity(request, year):
    return HttpResponse( qf.statistics(False, True, year) )

def req_qa_index_start_from(request, year, nof_questions, start_from):
    nof_registered_questions = qf.get_nof_questions(year)
    return req_qa_index_start_end(request, year, nof_questions, start_from, nof_registered_questions)

def req_qa_index_start_end(request, year, nof_questions, start, end):
    questions = get_question_list(nof_questions, start, end, year)
    return render_qa(request, questions, year)

def req_qa_questions_answers(request, year, nof_questions):
    nof_registered_questions = qf.get_nof_questions(year)
    questions = get_question_list(nof_questions, 1, nof_registered_questions, year)
    return render_qa(request, questions, year)

def req_qa_by_type(request, year, qtype, nof_questions):
    return req_qa_by_type_complexity(request, year, qtype, None, nof_questions)

def req_qa_by_complexity(request, year, complexity, nof_questions):
    return req_qa_by_type_complexity(request, year, None, complexity, nof_questions)

def req_qa_by_type_complexity(request, year, qtype, complexity, nof_questions):
    nof_registered_questions = qf.get_nof_questions(year)
    nof_questions = min(nof_questions, nof_registered_questions)
    questions = qf.ask_filtered(nof_questions, qtype, complexity, year)
    return render_qa(request, questions, year)

def get_question_list(nof_questions, start, end, year):
    nof_registered_questions = qf.get_nof_questions(year)
    nof_questions = min(nof_questions, nof_registered_questions)
    return qf.ask_question(nof_questions, start, end, year) #return list of questions

def render_qa(request, questions, year):
    header_str = "<!DOCTYPE html>"\
                "<title> Review Your Maths for year "+str(year)+" </title>"\
                "<head>"\
                    "{% load static %}"\
                    "<link rel=\"stylesheet\" href=\"{% static 'questions/css/the.css' %}\">"\
                    "<script src=\"{% static 'questions/js/eval_and_submit.js'%}\"></script>"\
                "</head><body><form autocomplete=\"off\" method=\"POST\" onsubmit=\"event.preventDefault();\" >{% csrf_token %}<ol>"
    hdr_template = Template(header_str)
    response = hdr_template.render(RequestContext(request,{}))
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
    response += "</ol></form></body>"
    return HttpResponse(response)

