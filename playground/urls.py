####map urls to view functions  
from django.urls import path  
from . import views

#URLConf, connect to project url.py file
urlpatterns = [ 
    path('hello/',views.say_hello)
]