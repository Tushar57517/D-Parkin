from django.urls import path
from .views import *

urlpatterns = [
    path('vehicle/', VehicleView.as_view(), name="vehicle"),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name="vehicle_by_id"),
    path('vehicle/<int:pk>/send-otp/', VehicleOTPView.as_view(), name="send_otp"),
    path('vehicle/<int:pk>/exit/', VehicleExitView.as_view(), name="vehicle_exit"),
]
