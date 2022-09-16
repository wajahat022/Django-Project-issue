from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=122)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=12)
    date = models.DateField()