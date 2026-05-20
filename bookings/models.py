from django.db import models
from accounts.models import User
from services.models import Service
from django.utils import timezone
timezone.now

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')


    def __str__(self):
        return f"{self.user} booked {self.service}"