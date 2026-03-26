from django.contrib import admin

from apps.dentists.models import Dentist

# Register your models here.


@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_time', 'end_time', 'user']
    search_fields = ['name']
    list_filter = ['user']
