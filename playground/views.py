from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function takes in a request and returns a response
# a "request handler" 
# request -> response 
# request handler. In many frameworks this is called an "action"
# django uses templates the way that other frameworks use views 

def calculate():
    x = 1 
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Jordan'})