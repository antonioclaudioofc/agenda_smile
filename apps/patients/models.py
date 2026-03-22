from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)