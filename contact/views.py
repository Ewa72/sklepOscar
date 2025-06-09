from django.shortcuts import render

# Create your views here.
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())