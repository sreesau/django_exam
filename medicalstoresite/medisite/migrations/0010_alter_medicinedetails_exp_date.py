# Generated by Django 5.0.1 on 2024-02-09 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medisite', '0009_alter_medicinedetails_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 8, 23, 46, 49, 703218)),
        ),
    ]
