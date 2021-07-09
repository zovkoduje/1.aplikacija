from django.db import models
from django.db.models.fields import BooleanField
import random

# Create your models here.

class Profesor(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Predmet(models.Model):
    naziv_predmeta = models.CharField(max_length=30)
    broj_ectsa = models.IntegerField()
    semestar_predmeta = models.IntegerField()
    obavezan_predmet = models.BooleanField()

    nositelj = models.OneToOneField(Profesor , on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_predmeta

class Student(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()
    adresa = models.CharField(max_length=30)
    grad = models.CharField(max_length=30)
    redovan_student = models.BooleanField(default=True)
    broj_ostvarenih_ectsa = models.IntegerField(null = True)
    #semestar studija trebat ce se automatski izracunavat temeljem broja ostvarenih ects bodova
    semestar_studija = models.IntegerField(null = True, default=5)
    predmet= models.ManyToManyField(Predmet)
    broj_xice=models.CharField(max_length=10, default=1)

    def __str__(self):
        return self.broj_xice


    