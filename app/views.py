from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

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


def insert_topic(request):
    TOI=input('Enter the data :')
    TO=Topic.objects.get_or_create(topic_name=TOI)[0]
    TO.save()
    NTO=Topic.objects.all()
    d={'topics':NTO}
    return render(request,'display.html',d)

def insert_webpage(request):
    WOI=input('Enter topic')
    NOI=input('Enter name')
    UOI=input('Enter URL')
    WPO=Topic.objects.get(topic_name=WOI)
    WO=Webpage.objects.get_or_create(topic_name=WPO,name=NOI,url=UOI)[0]
    WO.save()
    WWI=Webpage.objects.all()
    d={'wepa':WWI}
    return render(request,'web.html',d)

def insert_accessrecord(request):
    NOO=int(input('ENTER pk'))
    AOD=input('Enter Date')
    AOA=input('Enter author name')
    NOAA=Webpage.objects.get(pk=NOO)
    ACO=AccessRecord.objects.get_or_create(name=NOAA,date=AOD,Author=AOA)[0]
    ACO.save()
    ACCIO=AccessRecord.objects.all()
    d={'access':ACCIO}
    return render(request,'acc.html',d)








