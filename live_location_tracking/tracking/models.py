# tracking/models.py
from django.db import models
from django.contrib.auth.models import User

class LocationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.latitude}, {self.longitude}"
