from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django! This is Day 2.")

def about(request):
    return HttpResponse("This is the about page.")

def services(request):
    return HttpResponse("This is the services page.")

def contact(request):
    return HttpResponse("This is the contact page.")

