from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    car_number = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_number
    