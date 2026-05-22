from django.shortcuts import render
from django.http import HttpResponse 

#Importing Loader from template to display html pages
from django.template import loader

# Create your views here.
def fun_1(request):
    return HttpResponse("1st View")
def fun_2(request):
    return HttpResponse("Second View")
#func to display html
def fun_3(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())