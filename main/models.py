from django.db import models
from django.db.models.fields import BooleanField
import random

# Create your models here.

class Profesor(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()

class Predmet(models.Model):
    predmet_id = models.CharField(max_length=10, default=random.randint(1 , 10000) , unique=True , null=True)
    naziv_predmeta = models.CharField(max_length=30)
    broj_ectsa = models.IntegerField()
    semestar_predmeta = models.IntegerField()
    obavezan_predmet = models.BooleanField()

    nositelj = models.OneToOneField(Profesor , on_delete=models.CASCADE)

class Student(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()
    adresa = models.CharField(max_length=30)
    grad = models.CharField(max_length=30)
    redovan_student = models.BooleanField(default=True)
    broj_ostvarenih_ectsa = models.IntegerField(null = True)
    #semestar studija trebat ce se automatski izracunavat temeljem broja ostvarenih ects bodova
    semestar_studija = models.IntegerField(null = True)

    #predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)


    