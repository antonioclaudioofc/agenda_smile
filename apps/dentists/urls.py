from rest_framework.routers import DefaultRouter

from apps.dentists.views import DentistViewSet

router = DefaultRouter()
router.register(r'', DentistViewSet, basename='dentists')

urlpatterns = router.urls
