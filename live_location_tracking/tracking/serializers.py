from rest_framework import serializers
from .models import LocationLog

class LocationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationLog
        fields = ['user', 'latitude', 'longitude', 'timestamp']
