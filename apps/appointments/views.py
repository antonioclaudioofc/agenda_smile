from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.appointments.models import Appointment
from apps.appointments.serializers import AppointmentSerializer

# Create your views here.


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
