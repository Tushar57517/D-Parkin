from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'car_number', 'phone_number', 'email', 'status', 'otp', 'created_at', 'updated_at','creator']
        read_only_fields = ['status', 'otp', 'creator', 'created_at', 'updated_at']

class VehicleExitSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)