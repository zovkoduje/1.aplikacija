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
    redovan_student =factory.Faker("boolean",chance_of_getting_true=80)
    broj_ostvarenih_ectsa = factory.Faker("pyint",min_value=91,max_value=120)
    broj_xice=factory.Faker("pyint", min_value=1000000000, max_value=9999999999)
    # semestar se treba automatski izracunati temeljem broja ostvarenih ectsa
    #semestar_studija = random.randrange(1,6)

    #predmet = factory.Iterator(Predmet.objects.all())

class ProfesorFactory(DjangoModelFactory):
    class Meta:
        model = Profesor
    
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("safe_email")