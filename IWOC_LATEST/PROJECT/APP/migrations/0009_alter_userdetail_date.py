# Generated by Django 4.1.3 on 2023-01-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_history_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='date',
            field=models.DateTimeField(),
        ),
    ]