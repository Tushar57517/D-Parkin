from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class Vehicle(models.Model):
    STATUS_CHOICES=[
        ('active','Active'),
        ('exited','Exited'),
    ]

    car_number = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, default="")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    otp = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_number
    
    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()
    