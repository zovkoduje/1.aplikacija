from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from main.models import *
from django.views.generic import ListView
from rest_framework import viewsets
from main.serializers import *
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def homepage(request):
    return render(request , 'index.html')

def odabir_predmeta(request):

    lista_predmeta = Predmet.objects.all()

    context = {'lista_predmeta' : lista_predmeta}

    return render(request, 'main/odabir_predmeta.html' , context = context)

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

class PredmetList(ListView):
    model=Predmet

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)