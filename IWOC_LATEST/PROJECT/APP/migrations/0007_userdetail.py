# Generated by Django 4.1.3 on 2023-01-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_exefiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
