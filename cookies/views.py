from django.shortcuts import render
from django.http import HttpResponse


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('SUDHEER', 'klh.com')
    return response


def getcookie(request):
    name = request.COOKIES['SUDHEER']
    return HttpResponse("klh @: " + name);


