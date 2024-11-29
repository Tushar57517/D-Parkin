from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework import status

class RegisterView(APIView):
    permission_classes = []

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = []

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_200_OK)
        return Response({"error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# class HomeView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message":"Hello, World!"})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message":"successfully logged out"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error":"token not found"}, status=status.HTTP_400_BAD_REQUEST)