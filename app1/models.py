from django.db import models
from datetime import date

# Create your models here.

class vote(models.Model):
    gender_cho = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ) 
    name = models.CharField(max_length=50)
    
    gender = models.CharField(max_length=9, choices = gender_cho, null=True, blank=True )
    date_of_birth = models.DateField()
    aadhar = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=80)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    voter_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
