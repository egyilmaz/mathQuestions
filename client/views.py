from django.http import HttpResponse
from django.template import loader

def landing_page(request):
    template = loader.get_template('client/landing.html')
    context = {
        'app_name': 'Review Questions App',
    }
    return HttpResponse(template.render(context, request))