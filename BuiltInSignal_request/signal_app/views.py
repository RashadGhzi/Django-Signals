from django.shortcuts import render, HttpResponse


def home(request):
    # a = 10/0 #This is for request exception error
    return HttpResponse('People is nothing')
