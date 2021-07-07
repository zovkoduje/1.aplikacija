from django.db.models import fields
from rest_framework import serializers

from main.models import *

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('ime' , 'prezime' , 'email' , 'adresa', 'grad' , 'redovan_student' , 'broj_ostvarenih_ectsa' , 'semestar_studija')
    
class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesor
        fields = ('ime' , 'prezime' , 'email')

class PredmetSerializer(serializers.HyperlinkedModelSerializer):
    model = Predmet
    fields = ('predmet_id', 'naziv_predmeta' , 'broj_ectsa' , 'semestar_predmeta' , 'obavezan_predmet' , 'nositelj')