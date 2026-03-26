from django.utils import timezone

from rest_framework import serializers

from apps.appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate(self, attrs):
        request = self.context['request']
        user = request.user

        start_time = attrs.get('start_time', getattr(
            self.instance, 'start_time', None)
        )
        end_time = attrs.get('end_time', getattr(
            self.instance, 'end_time', None)
        )
        date = attrs.get('date', getattr(self.instance, 'date', None))
        patient = attrs.get('patient', getattr(self.instance, 'patient', None))
        dentist = attrs.get('dentist', getattr(self.instance, 'dentist', None))

        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError(
                'Hora inicial deve ser menor que hora final'
            )

        if date == timezone.localdate():
            now_time = timezone.localtime().time()

            if start_time and start_time < now_time:
                raise serializers.ValidationError(
                    'Não é possível agendar horário no passado'
                )

        if patient and patient.user != user:
            raise serializers.ValidationError('Paciente inválido')

        if dentist and dentist.user != user:
            raise serializers.ValidationError('Dentista inválido')

        if dentist and start_time and end_time:
            if start_time < dentist.start_time or end_time > dentist.end_time:
                raise serializers.ValidationError(
                    'Horário fora da agenda do dentista'
                )

        if dentist and date and start_time and end_time:
            query = Appointment.objects.filter(
                dentist=dentist,
                date=date,
            )

            if self.instance:
                query = query.exclude(pk=self.instance.pk)

            conflict = query.filter(
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exists()

            if conflict:
                raise serializers.ValidationError(
                    'Já existe um agendamento nesse horário')
        return attrs
