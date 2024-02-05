from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from .models import News
from .serializers import NewsSerializers
from .permission import NewsPermission

# Create your views here.



class NewsAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    
    
    def preform_create(self, serializers):
        return serializers.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (NewsPermission(), )
        return (AllowAny(), )