from django.http import HttpResponse
from django.template import Template, RequestContext
from django.http import JsonResponse
from .models import User
from questions.src.question.QuestionFactory import QuestionFactory
import random


def get_questions_csv():
    questions = list(range(1,nof_registered_questions+1))
    random.shuffle(questions)
    csv = str(questions[0])
    for i in questions[1:]:
        csv += ","+str(i)
    return csv


def get_next_question(questions_csv):
    questions = questions_csv.split(",")
    qf = QuestionFactory()
    return qf.ask_question(1, int(questions[0]), int(questions[0])) #return list of questions


def reset_questions(request, username):
    try:
        current_user = User.objects.get(user_name=username)
        current_user.questions=get_questions_csv()
        current_user.save()
        return render_qa(request, get_next_question(current_user.questions))
    except User.DoesNotExist:
        return HttpResponse("No such user")


def home_page(request, username):
    try:
        current_user = User.objects.get(user_name=username)
        return render_qa( request, get_next_question(current_user.questions))
    except User.DoesNotExist:
        user = User(user_name=username, questions=get_questions_csv())
        user.save() # save it to db.
        return render_qa( request, get_next_question(user.questions))


def json_response(q):
    text = q.question()
    graphic = q.graphic()
    meta = q.meta()
    answer = q.answer()
    answer_graphic = q.answer_graphic()
    return JsonResponse( {"text": text, "graphic": graphic, "meta": meta, "answer": answer, "answer_graphic": answer_graphic} )


def render_qa(request, q):
    return json_response(q[0])


def render_question(request,q):
    header_str = "<!DOCTYPE html>" \
                 "<title> Review Your Maths </title>" \
                 "<head>" \
                 "{% load static %}" \
                 "<link rel=\"stylesheet\" href=\"{% static 'user/css/the.css' %}\">" \
                 "<script src=\"{% static 'user/js/eval_and_submit.js'%}\"></script>" \
                 "</head><body><form autocomplete=\"off\" method=\"POST\" onsubmit=\"event.preventDefault();\" >{% csrf_token %}"
    hdr_template = Template(header_str)
    response = hdr_template.render(RequestContext(request, {}))
    template = q.template()
    context = q.context()
    c = RequestContext(request, context)
    response += template.render(c)
    response += "</form></body></html>"
    return HttpResponse(response)