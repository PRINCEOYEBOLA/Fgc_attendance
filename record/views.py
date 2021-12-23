from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is an application about record keeping')

def about(request):
    return HttpResponse('This is an application that helps in keeping data of members')
