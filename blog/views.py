from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return HttpResponse('')


def post(request):
    return HttpResponse('')
