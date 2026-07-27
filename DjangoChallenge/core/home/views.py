from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "name": "Sanskar Acharya",
        "description": "Learning Django one day at a time and documenting everything on GitHub.",
        "button": "Explore",
        "year": 2026,
        "author": "Sanskar Acharya",
        "challenge": "100 Days of Django"
    }
    
    return render(request, 'index.html', context)

def about(request):
    context ={
        "skills": ["Python", "Django", "HTML", "CSS", "C", "C++"],
    }
    return render(request, 'about.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

