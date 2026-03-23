from rest_framework import serializers

from apps.dentists.models import Dentist


class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time is not None and end_time is not None:
            if start_time >= end_time:
                raise serializers.ValidationError(
                    'Hora inicial deve ser menor que a final.'
                )

        return data
