import re

from rest_framework import serializers

from apps.patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_cpf(self, value):
        cpf = re.sub(r'\D', '', value)

        if len(cpf) != 11:
            raise serializers.ValidationError('CPF inválido.')

        return value

    def validate_phone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Telefone inválido')

        return value
