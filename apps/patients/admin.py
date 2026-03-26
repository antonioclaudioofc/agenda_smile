from django.contrib import admin

from apps.patients.models import Patient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'cpf', 'phone', 'user']
  list_filter = ['id', 'name', 'phone', 'user']
  search_fields = ['user']
