# Generated by Django 3.1.7 on 2021-07-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_predmet_predmet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predmet',
            name='predmet_id',
            field=models.CharField(default=8836, max_length=10, null=True, unique=True),
        ),
    ]
