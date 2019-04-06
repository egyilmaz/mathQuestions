from django.http import HttpResponse
from django.template import loader
from .src.question.QuestionFactory import QuestionFactory, nof_registered_questions
from .src.question.Types import Output

def index(request, nof_questions):
    return index_start_end(request, nof_questions, 1, nof_registered_questions)

def index_start_from(request, nof_questions, start_from):
    return index_start_end(request, nof_questions, start_from, nof_registered_questions)

def get_question_list(nof_questions, start, end):
    qf = QuestionFactory(Output.ONLINE)
    return qf.ask(nof_questions, start, end) #return list of questions
    

def index_start_end(request, nof_questions, start, end):
    questions = get_question_list(nof_questions, start, end)
    result=[]
    for q in questions:
        result.append((q.question(),q.graphic()))
    template = loader.get_template("questions/questions.html")
    context = {"questions_list":result}
    return HttpResponse(template.render(context,request))

def questions_answers(request, nof_questions):
    questions = get_question_list(nof_questions, 1, nof_registered_questions)
    result=[]
    for q in questions:
        result.append((q.question(),q.graphic(),q.meta(),q.answer()))
    template = loader.get_template("questions/qa.html")
    context = {"questions_list":result}
    return HttpResponse(template.render(context,request))

def evaluate(request):
   if request.method == 'POST':
        user_input = request.POST.get('user_input', None)
        correct_answer = request.POST.get('correct_answer', None)
        meta = request.POST.get('meta', None)
        return HttpResponse("Input "+user_input+"<br><br>Correct answer "+correct_answer+"<br><br>Meta "+meta)

