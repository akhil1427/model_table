from django.shortcuts import render
from app.models import *

# Create your views here.

def display(request):

    TOO=Topic.objects.all()
    d={'topics':TOO}
    return render(request,'display.html',d)


def web(request):

    WEBPA=Webpage.objects.all()
    d={'wepa':WEBPA}
    return render(request,'web.html',d)


def acc(request):

    ACCTO=Webpage.objects.all()
    d={'access':ACCTO}
    return render(request,'acc.html',d)

