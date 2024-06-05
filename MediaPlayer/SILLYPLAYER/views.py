from django.shortcuts import render
from django.http import HttpRequest, request

# Create your views here.
def sillyplayer(request):
    return render(request,'sillyplayer.html');

