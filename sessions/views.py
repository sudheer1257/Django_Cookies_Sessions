from django.shortcuts import render
from django.http import HttpResponse


def setsession(request):
    request.session['sname'] = 'sudheer'
    request.session['semail'] = 'sudheer@gmail.com'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname + " " + studentemail);