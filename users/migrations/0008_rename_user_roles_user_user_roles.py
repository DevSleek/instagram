# Generated by Django 4.2.1 on 2023-07-31 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_roles',
            new_name='user_roles',
        ),
    ]
