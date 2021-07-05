from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path("" , homepage, name = "homepage"),
    path("students" , StudentList.as_view())
]