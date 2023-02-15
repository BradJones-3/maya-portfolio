from django.shortcuts import render
from django.http import HttpResponse

from models import *


def registerPage(request):
    context = {}
    return render(request, 'profiles/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'profiles/login.html', context)
