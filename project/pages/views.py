from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello from index page via HTTP response")

def about(request):
    return HttpResponse("Hello from about page via HTTP response")