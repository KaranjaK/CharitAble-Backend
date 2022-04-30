from django.shortcuts import render
from django.core.mail import send_mail


send_mail('Welcome mail', 'Welcome to charitable , where you get to support and get support.', 'from@example.com', ['to@example.com'], fail_silently=False)


# Create your views here.
