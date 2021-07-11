from django.db.models import fields
from main.models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['predmet']


