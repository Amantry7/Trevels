from rest_framework.viewsets import GenericViewSet 
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer

# Create your views here.
class HotelAPI(GenericViewSet, 
               mixins.ListModelMixin, 
               mixins.RetrieveModelMixin):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_class = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_filds = ['title', 'description']
    
    
    