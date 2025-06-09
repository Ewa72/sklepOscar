from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())