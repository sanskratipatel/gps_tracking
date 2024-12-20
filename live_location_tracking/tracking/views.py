# tracking/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LocationLog
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

 # Assume this is where your location logs are stored

def get_latest_location(request, user_id):
    # Get the latest location log for the user
    location = LocationLog.objects.filter(user_id=user_id).latest('timestamp')
    
    data = {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'timestamp': location.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return JsonResponse(data)


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import LocationLog
from django.utils.timezone import localtime

def profile_view(request, user_id):
    # Retrieve the user by ID
    user = get_object_or_404(User, id=user_id)

    # Get the most recent location log for the user
    location_log = LocationLog.objects.filter(user=user).order_by('-timestamp').first()

    # Get the user's date of joining
    date_joined = user.date_joined

    # Pass the data to the template
    return render(request, 'user_profile.html', {
        'user': user,
        'location_log': location_log,
        'date_joined': date_joined,
    })


