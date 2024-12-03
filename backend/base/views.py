from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

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
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk, creator=request.user)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    
class VehicleOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        vehicle=get_object_or_404(Vehicle, pk=pk, creator=request.user)
        vehicle.generate_otp()

        send_mail(
            'Vehicle Exit OTP',
            f'Your OTP for vehicle exit is {vehicle.otp}',
            'ts3883372@gmail.com',
            [vehicle.email],
            fail_silently=False,
        )
        return Response({"message":"OTP send to registered email"}, status=status.HTTP_200_OK)
    
class VehicleExitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        vehicle =  get_object_or_404(Vehicle, pk=pk, creator=request.user)
        serializer = VehicleExitSerializer(data=request.data)

        if serializer.is_valid():
            if vehicle.otp == serializer.validated_data['otp']:
                vehicle.status = 'exited'
                vehicle.save()
                return Response({"message":"Vehicle exited successfully"}, status=status.HTTP_200_OK)
            return Response({"message":"Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)