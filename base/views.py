from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def ru(request):
    return render(request, 'base/ru.html')