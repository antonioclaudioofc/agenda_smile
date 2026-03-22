from django.db import models

from apps.dentists.models import Dentist
from apps.patients.models import Patient
from django.contrib.auth.models import User

# Create your models here.


class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'agendado'),
            ('completed', 'Concluído'),
            ('canceled', 'Cancelado')
        ],
        default='scheduled'
    )

    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('dentist', 'date', 'time')
