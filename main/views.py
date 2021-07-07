from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from main.models import *
from django.views.generic import ListView
from rest_framework import viewsets
from main.serializers import *

# Create your views here.

def homepage(request):
    return render(request , 'index.html')

class StudentList(ListView):
    model = Student

class ProfesorList(ListView):
    model = Profesor

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('prezime')
    serializer_class = StudentSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all().order_by('prezime')
    serializer_class = ProfesorSerializer

class PredmetViewSet(viewsets.ModelViewSet):
    queryset = Predmet.objects.all().order_by('naziv_predmeta')
    serializer_class = PredmetSerializer