from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from main.models import *
from django.views.generic import ListView

# Create your views here.

def homepage(request):
    return HttpResponse("<h1> Hoempage </h1>")

class StudentList(ListView):
    model = Student