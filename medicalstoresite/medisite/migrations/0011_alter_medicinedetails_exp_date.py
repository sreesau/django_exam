# Generated by Django 5.0.6 on 2024-06-06 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medisite', '0010_alter_medicinedetails_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2025, 6, 6, 18, 23, 55, 870922)),
        ),
    ]
