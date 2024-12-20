# users/views.py

from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.forms import AuthenticationForm
from .models import User



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User


class RegisterView(APIView):
    """
    Handle user registration via API or web form.
    """
    def get(self, request):
        # Render the HTML form for web users
        return render(request, "register.html")

    def post(self, request):
        # Extract username and email from the request
        username = request.data.get('username')
        email = request.data.get('email')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists. Please choose another."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already exists. Please choose another."
            })

        # If valid, save the new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, "register.html", {
                "success": "User registered successfully! Please log in."
            })

        # Return validation errors
        return render(request, "register.html", {
            "error": "Invalid data. Please correct the errors and try again.",
            "details": serializer.errors
        })

class LoginView(APIView):
    def get(self, request):
        # Render the login page template
        return render(request, 'login.html')

    def post(self, request):
        # Handle login request
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after successful login
            return Response({"error": "Invalid credentials"}, status=400)
        
        return Response(serializer.errors, status=400)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Fetch all users
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})


# def user_info(request, user_id):
#     if not request.user.is_authenticated:
#          return redirect('login')
    
#     # Fetch the specific user
#     user = get_object_or_404(User, id=user_id)
#     return render(request, 'user_detail.html', {'user': user})

# from django.shortcuts import render

