# # users/views.py

# from django.shortcuts import get_object_or_404, render, redirect
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer, LoginSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate, login, logout
# from .models import User
# from .serializers import UserSerializer, LoginSerializer
# from django.contrib.auth.forms import AuthenticationForm
# from .models import User



# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
# from .models import User


# class RegisterView(APIView):
#     """
#     Handle user registration via API or web form.
#     """
#     def get(self, request):
#         # Render the HTML form for web users
#         return render(request, "register.html")

#     def post(self, request):
#         # Extract username and email from the request
#         username = request.data.get('username')
#         email = request.data.get('email')

#         # Check if username or email already exists
#         if User.objects.filter(username=username).exists():
#             return render(request, "register.html", {
#                 "error": "Username already exists. Please choose another."
#             })

#         if User.objects.filter(email=email).exists():
#             return render(request, "register.html", {
#                 "error": "Email already exists. Please choose another."
#             })

#         # If valid, save the new user
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(request, "register.html", {
#                 "success": "User registered successfully! Please log in."
#             })

#         # Return validation errors
#         return render(request, "register.html", {
#             "error": "Invalid data. Please correct the errors and try again.",
#             "details": serializer.errors
#         })

# class LoginView(APIView):
#     def get(self, request):
#         # Render the login page template
#         return render(request, 'login.html')

#     def post(self, request):
#         # Handle login request
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('dashboard')  # Redirect to dashboard after successful login
#             return Response({"error": "Invalid credentials"}, status=400)
        
#         return Response(serializer.errors, status=400)

# def dashboard(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
    
#     # Fetch all users
#     users = User.objects.all()
#     return render(request, 'dashboard.html', {'users': users})


from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from .models import User
import random

# Store OTPs temporarily (consider using a database table in production)
otp_storage = {}

class RegisterView(APIView):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists. Please choose another."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already exists. Please choose another."
            })

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, "register.html", {
                "success": "User registered successfully! Please log in."
            })
        if User.objects.filter(email=email, username=username).exists():
             return render(request, "register.html", {
            "error": "Username and email already exist. Please Login."
             })

        return render(request, "register.html", {
            "error": "Invalid data. Please correct the errors and try again.",
            "details": serializer.errors
        })



# from django.contrib.auth import authenticate, login
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .serializers import LoginSerializer

# class LoginView(APIView):
#     def get(self, request):
#         # Render the login page template
#         return render(request, 'login.html')

#     def post(self, request):
#         # Handle login request
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
            
#             # Try to authenticate user by username
#             user = authenticate(username=username, password=password)
            
#             if user:
#                 login(request, user)
#                 return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response({"error": "Invalid form submission."}, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import LoginSerializer
from django.shortcuts import render

class LoginView(APIView):
    def get(self, request):
        # Render the login page template
        return render(request, 'login.html')

    def post(self, request):
        # Handle login request
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data['username_or_email']
            password = serializer.validated_data['password']
            
            # Try to authenticate user by username or email
            if '@' in username_or_email:  # If it's an email, try to find the user by email
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    return Response({"error": "Invalid username or email or password."}, status=status.HTTP_401_UNAUTHORIZED)
            else:  # Otherwise, treat it as a username
                user = authenticate(username=username_or_email, password=password)

            # Check if the user exists and the password is correct
            if user and user.check_password(password):
                login(request, user)
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid username or email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"error": "Invalid form submission."}, status=status.HTTP_400_BAD_REQUEST)

# class ForgotPasswordView(APIView):
#     """
#     Handle forgot password by sending OTP to user's email.
#     """
#     def get(self, request):
#         # Render the Forgot Password page
#         return render(request, 'forgot_password.html')

#     def post(self, request):
#         email = request.data.get('email')
#         user = User.objects.filter(email=email).first()

#         if user:
#             # Generate OTP
#             otp = random.randint(100000, 999999)
#             otp_storage[email] = otp  # Store OTP in the temporary storage (ideally use a secure storage)

#             # Send OTP via email
#             send_mail(
#                 subject="Your Password Reset OTP",
#                 message=f"Your OTP is {otp}. Do not share it with anyone.",
#                 from_email="noreply@example.com",  # Replace with your actual email
#                 recipient_list=[email]
#             )

#             # Render the OTP verification page
#             return render(request, 'verify_otp.html', {'email': email})
        
#         # If the email does not exist, show an error message
#         return render(request, 'forgot_password.html', {"error": "Email not found."})

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views import View
# from django.core.cache import cache  # Using cache for temporary OTP storage

# class VerifyOtpView(View):
#     def post(self, request):
#         email = request.POST.get('email')
#         otp = request.POST.get('otp')

#         # Retrieve the stored OTP from cache
#         stored_otp = cache.get(email)

#         if stored_otp and stored_otp == otp:
#             # OTP is correct, return success response
#             return JsonResponse({'success': True, 'email': email})
#         else:
#             # OTP is incorrect
#             return JsonResponse({'success': False}, status=400)  

import random
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.cache import cache

class ForgotPasswordView(APIView):
    """
    Handle forgot password by sending OTP to user's email.
    """
    def get(self, request):
        # Render the Forgot Password page
        return render(request, 'forgot_password.html')

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            # Generate OTP
            otp = str(random.randint(100000, 999999))  # Ensure OTP is a string
            cache.set(email, otp, timeout=300)  # Store OTP in cache for 5 minutes

            # Send OTP via email
            send_mail(
                subject="Your Password Reset OTP",
                message=f"Your OTP is {otp}. Do not share it with anyone.",
                from_email="noreply@example.com",  # Replace with your actual email
                recipient_list=[email]
            )

            # Render the OTP verification page
            return render(request, 'verify_otp.html', {'email': email})
        
        # If the email does not exist, show an error message
        return render(request, 'forgot_password.html', {"error": "Email not found."})

from django.http import JsonResponse
from django.views import View
from django.core.cache import cache

class VerifyOtpView(View):
    def post(self, request):
        email = request.POST.get('email')
        otp = request.POST.get('otp').strip()  # Strip any whitespace

        # Retrieve the stored OTP from cache
        stored_otp = cache.get(email)

        # Debugging output
        print(f"Stored OTP: {stored_otp}, Entered OTP: {otp}")  # Log the values for debugging

        if stored_otp and stored_otp == otp:
            # OTP is correct, return success response
            return JsonResponse({'success': True, 'email': email})
        else:
            # OTP is incorrect
            return JsonResponse({'success': False}, status=400)
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ChangePasswordView(APIView):
    """
    Allow user to set a new password after verifying OTP.
    """
    def get(self, request):
        email = request.GET.get('email')
        return render(request, 'change_password.html', {'email': email})

    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        # Check if passwords match
        if new_password != confirm_password:
            return render(request, 'change_password.html', {
                "error": "Passwords do not match. Please try again.",
                "email": email
            })

        # Check if the new password is different from the old one
        user = User.objects.filter(email=email).first()
        if user and not check_password(new_password, user.password):
            user.set_password(new_password)
            user.save()

            # Clear OTP after successful password reset
            cache.delete(email)  # Clear OTP from cache

            return render(request, 'login.html', {"success": "Password reset successful! Please log in."})
        
        # If new password is same as the old one, show an error
        return render(request, 'change_password.html', {
            "error": "New password cannot be the same as the old password.",
            "email": email
        })


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Fetch all users
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})
