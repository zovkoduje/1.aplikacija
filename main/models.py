from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Profesor(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()

class Predmet(models.Model):
    naziv_predmeta = models.CharField(max_length=30)
    broj_ectsa = models.IntegerField()
    semestar_predmeta = models.IntegerField()
    obavezan_predmet = models.BooleanField()

    nositelj = models.OneToOneField(Profesor , on_delete=models.CASCADE)

class Student(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()
    redovan_student = models.BooleanField()
    broj_ostvarenih_ectsa = models.IntegerField()
    semestar_studija = models.IntegerField()

    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)


    