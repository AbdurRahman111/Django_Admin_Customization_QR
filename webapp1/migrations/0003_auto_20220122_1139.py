# Generated by Django 2.1.5 on 2022-01-22 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0002_auto_20220122_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifica_risultati_candidato',
            name='DATA_DI_NASCITA',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 22, 11, 39, 12, 464167)),
        ),
    ]
