# Generated by Django 4.1.3 on 2023-01-11 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0012_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
