from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html', {'name':"Yurii"})

def empty(request):
    return HttpResponse('')

# Create your views here.
