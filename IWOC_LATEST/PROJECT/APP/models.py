from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import transaction
from django.db.models import F, Max
# Create your models here.
from django import forms


class User(AbstractUser):
    is_superadmin= models.BooleanField('Is superadmin', default=False)
    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    
    role = models.CharField(max_length=10,
    choices= [('SuperAdmin','SuperAdmin'),('Admin','Admin'),('User','User')])


status_choices=(
    ('enables','ENABLED'),('disaabled','DISSABLED'),)

    


freq_choices=(
    ('All','All'),('Cycle','Cycle'),('Daily','Daily'),
    ('Monthly','Monthly'),('Quarterly','Quarterly'),('Yearly','Yearly'))

class Scheduler(models.Model):
    ID=models.IntegerField(primary_key=True)
    FILE_NAME =models.CharField(max_length=200)
    UNIQUE_NAME=models.CharField(max_length=200)
    PROGRAM_NAME=models.CharField(max_length=200)
    CLIENT_NAME=models.CharField(max_length=200)
    JOB_TITLE=models.CharField(max_length=200)
    FREQUENCY=models.CharField(choices=freq_choices,max_length=200)
    STATUS=models.CharField(choices=status_choices,max_length=200)
    OUT_FILE_DIRECTORY=models.CharField(max_length=200)


class ProgFile(models.Model):    
    ID=models.IntegerField(primary_key=True)
    FILE_NAME =models.CharField(max_length=200)
    PROGRAM_NAME=models.CharField(max_length=200)

class History(models.Model):
    JobIDX=models.IntegerField(primary_key=True)
    Date =models.DateField()
    Start=models.CharField(max_length=200)
    Finish=models.CharField(max_length=200)
    User=models.CharField(max_length=200)
    Product=models.CharField(max_length=200)
    File=models.CharField(max_length=200)
    Status=models.CharField(max_length=200)
    Log=models.CharField(max_length=200)
    ActiveCount=models.CharField(max_length=200)
    Page=models.CharField(max_length=200)
    Impression=models.CharField(max_length=200)
    username = models.CharField(max_length=100)


class EXEFILES(models.Model):
    exename = models.CharField(max_length=100)

    def __str__(self):
        return self.exename


# class UserDetails(models.Model):
#     ID = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     outcome = models.DateTimeField()
#     acti = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username



class DetailActivity(models.Model):
    ID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    logidate = models.DateTimeField()
    logodate = models.DateTimeField()
    acti = models.CharField(max_length=100)


    def __str__(self):
        return self.username