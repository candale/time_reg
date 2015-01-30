from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext


def index(request):
    return HttpResponse("lol, index")
