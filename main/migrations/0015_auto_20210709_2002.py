# Generated by Django 2.2.12 on 2021-07-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210709_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='broj_xice',
            field=models.CharField(max_length=10),
        ),
    ]