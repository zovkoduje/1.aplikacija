from django.contrib import admin
from main.models import *

# Register your models here.

models = [Student , Predmet , Profesor]

admin.site.register(models)