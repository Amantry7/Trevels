from rest_framework.routers import  DefaultRouter
from apps.hotels.views import HotelAPI

router = DefaultRouter()

router.register('hotel', HotelAPI, basename='api_hotel')


urlpatterns = router.urls
