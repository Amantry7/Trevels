from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.tours.models import Tour
from apps.tours.serializers import TourSerializers

# Create your views here.
class TourViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers