from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

class VehicleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vehicles = Vehicle.objects.filter(creator=request.user)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        data['creator'] = request.user.id
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk, creator=request.user)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)