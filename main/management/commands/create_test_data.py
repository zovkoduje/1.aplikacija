from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factory import *

NUM_STUDENTS = 140
NUM_PROFESORS = 10

class Command(BaseCommand):
    help = "Stvaranje testnih podataka"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brisanje starih podataka")
        models = [Student]

        for m in models:
            m.objects.all().delete()

        self.stdout.write("Stvaranje testnih podataka")

        for _ in range(NUM_STUDENTS):
            student = StudentFactory()
        
        for _ in range(NUM_PROFESORS):
            profesor = ProfesorFactory()
