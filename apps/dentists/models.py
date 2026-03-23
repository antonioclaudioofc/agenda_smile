from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Dentist(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Dentist'
        verbose_name_plural = 'Dentists'
