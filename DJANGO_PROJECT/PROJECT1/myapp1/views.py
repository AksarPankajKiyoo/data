from django.shortcuts import render
from django.http import HttpRequest, request

# Create your views here.

def welcomeFunction(request):
    return render(request, "index.html")
