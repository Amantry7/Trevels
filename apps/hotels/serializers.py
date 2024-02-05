from rest_framework import serializers

from apps.hotels.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel 
        fields = ('id', 'title', 'description',
                  'image', 'stars', 'tour')