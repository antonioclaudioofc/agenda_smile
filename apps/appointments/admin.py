from django.contrib import admin

from apps.appointments.models import Appointment

# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'dentist',
        'date',
        'start_time',
        'end_time',
        'status',
        'user'
    ]

    list_filter = ['date', 'dentist', 'status']
    search_fields = ['patient__name', 'dentist__name']
