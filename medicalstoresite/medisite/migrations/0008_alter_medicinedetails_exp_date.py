# Generated by Django 5.0.1 on 2024-02-08 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medisite', '0007_alter_medicinedetails_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 7, 16, 13, 27, 99257)),
        ),
    ]
