import factory
from factory.base import FactoryOptions
from factory.django import DjangoModelFactory
from main.models import *
import random

class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student
    
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("safe_email")
    adresa = factory.Faker("address")
    grad = factory.Faker("city")
    redovan_student = random.choice([True, False])
    broj_ostvarenih_ectsa = random.randrange(0,180)
    # semestar se treba automatski izracunati temeljem broja ostvarenih ectsa
    #semestar_studija = random.randrange(1,6)

    #predmet = factory.Iterator(Predmet.objects.all())

class ProfesorFactory(DjangoModelFactory):
    class Meta:
        model = Profesor
    
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("safe_email")