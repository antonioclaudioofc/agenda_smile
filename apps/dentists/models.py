from django.db import models

# Create your models here.

class Dentist(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()