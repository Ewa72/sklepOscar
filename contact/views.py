# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
#
#
# # Create your views here.
# def contact(request):
#     template = loader.get_template('contact.html')
#     return HttpResponse(template.render())
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email subject and message
            subject = f"New Contact from {name}"
            message_body = f"Message from {name} ({email}):\n\n{message}"

            # Send email
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                ['ewa07adamus@gmail.com']#['kontakt@pasiekanadjeziorem.pl'],  # Replace with the recipient's email
            )

            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})