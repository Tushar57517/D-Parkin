from django.urls import path
from .views import *

urlpatterns = [
    path('vehicle/', VehicleView.as_view(), name="vehicle"),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name="vehicle_by_id"),
]
