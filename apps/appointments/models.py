from django.db import models

from apps.dentists.models import Dentist
from apps.patients.models import Patient
from django.contrib.auth.models import User

# Create your models here.


class Status(models.TextChoices):
    SCHEDULED = 'scheduled', 'Agendado'
    COMPLETED = 'completed', 'Concluído'
    CANCELED = 'canceled', 'Cancelado'


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'start_time']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"{self.patient} - {self.date} {self.start_time}"
