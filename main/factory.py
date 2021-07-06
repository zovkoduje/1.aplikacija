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
    #broj_ostvarenih_ectsa = factory.Faker("random_element")
    #semestar_studija = factory.LazyAttribute(random.randrange(1, 6))

    #predmet = factory.Iterator(Predmet.objects.all())