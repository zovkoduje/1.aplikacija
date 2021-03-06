# Generated by Django 2.2.12 on 2021-07-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210711_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='predmeti',
        ),
        migrations.AddField(
            model_name='predmet',
            name='nositelj_predmeta',
            field=models.ManyToManyField(to='main.Profesor'),
        ),
        migrations.AlterField(
            model_name='predmet',
            name='broj_ectsa',
            field=models.IntegerField(default=5),
        ),
    ]
