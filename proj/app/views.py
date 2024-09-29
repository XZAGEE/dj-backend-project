from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>hello wrld</h1>')
def empty(request):
    return HttpResponse('')

# Create your views here.
