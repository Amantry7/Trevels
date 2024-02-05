from rest_framework.routers import DefaultRouter

from apps.tours.views import TourViewSet 

router = DefaultRouter()
router.register('tour', TourViewSet, basename="api_tour")

urlpatterns = router.urls