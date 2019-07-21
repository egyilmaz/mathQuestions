from django.http import HttpResponse
from django.template import loader

def home_page(request,user):
    template = loader.get_template('user/index.html')
    context = {
        'app_name': 'Review Questions App',
    }
    return HttpResponse(template.render(context, request))