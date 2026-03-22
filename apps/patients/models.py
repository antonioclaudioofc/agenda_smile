from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=225)
    cpf = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
