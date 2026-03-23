from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.patients.models import Patient
from apps.patients.serializers import PatientSerializer

# Create your views here.


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Patient.objects.filter(
            user=self.request.user
        ).order_by('name')

        search = self.request.query_params.get('search')

        if search:
            queryset = self.queryset.filter(name__icontains=search)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
