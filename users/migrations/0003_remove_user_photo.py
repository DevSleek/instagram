# Generated by Django 4.2.1 on 2023-06-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_auth_status_user_auth_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]
