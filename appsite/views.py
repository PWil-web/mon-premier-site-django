from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def accueil(request):
    template = loader.get_template('appsite/index.html')
    return HttpResponse(template.render({}, request))
