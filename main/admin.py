from django.contrib import admin
from main.models import *

# Register your models here.

models = [Student , Predmet , Profesor, Predmeti_druge_godine]

admin.site.register(models)