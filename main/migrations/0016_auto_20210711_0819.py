# Generated by Django 2.2.12 on 2021-07-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210709_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predmet',
            name='nositelj',
        ),
        migrations.AddField(
            model_name='profesor',
            name='predmeti',
            field=models.ManyToManyField(to='main.Predmet'),
        ),
    ]