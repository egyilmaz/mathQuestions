from django.http import HttpResponse
from django.template import loader
from .src.question.QuestionFactory import QuestionFactory
from .src.question.Types import Output
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot():
    x=range(1,10)
    y=x
    plt.plot(x,y)
    buf = BytesIO()
    plt.savefig(buf, format='PNG', dpi=100)
    graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
    buf.close()
    return graphic
    
    

def index(request, nof_questions):
    qf = QuestionFactory(Output.ONLINE)
    result = qf.ask(nof_questions) #return list of questions
    template = loader.get_template("questions/questions.html")
    graphic = plot()
    context = {"questions_list":result,'graphic':graphic}
    return HttpResponse(template.render(context,request))

