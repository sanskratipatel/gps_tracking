# tracking/routing.py

from django.urls import path
from .consumers import LocationTrackingConsumer

websocket_urlpatterns = [
    path('ws/location/', LocationTrackingConsumer.as_asgi()),
]
