# Generated by Django 4.2.1 on 2024-02-09 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userconfirmation_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfirmation',
            name='expiration_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]