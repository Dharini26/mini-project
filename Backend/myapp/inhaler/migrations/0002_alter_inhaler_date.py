# Generated by Django 5.0.6 on 2024-06-08 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inhaler", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inhaler",
            name="date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
