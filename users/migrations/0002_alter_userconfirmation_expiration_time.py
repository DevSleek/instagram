# Generated by Django 4.2.1 on 2024-02-08 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfirmation',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 16, 30, 31, 783865)),
        ),
    ]
