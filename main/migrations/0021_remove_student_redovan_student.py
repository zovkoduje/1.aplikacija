# Generated by Django 2.2.12 on 2021-07-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210711_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='redovan_student',
        ),
    ]
