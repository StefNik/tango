from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br /> <a href='./about'>click here </a>")


def about(request):
    return HttpResponse("Rango says here is the about page. <br /> <a href='../'>click here </a>")
