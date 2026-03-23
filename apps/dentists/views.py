from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.dentists.models import Dentist
from apps.dentists.serializers import DentistSerializer

# Create your views here.


class DentistViewSet(ModelViewSet):
    serializer_class = DentistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Dentist.objects.filter(
            user=self.request.user
        ).order_by('name')

        search = self.request.query_params.get('search')

        if search:
            queryset = self.queryset.filter(name__icontains=search)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
