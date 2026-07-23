from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! This is Day 2.")

# Create your views here.
