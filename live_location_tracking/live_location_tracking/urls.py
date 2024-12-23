"""
URL configuration for live_location_tracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# live_location_tracking/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views as user_views
from tracking import views as tracking_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirect root to login
    path('admin/', admin.site.urls),
    path('register/', user_views.RegisterView.as_view(), name='register'),
    path('login/', user_views.LoginView.as_view(), name='login'),  # Corrected path
    # path('api/location/', tracking_views.LocationUpdateView.as_view(), name='location_update'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    # path('user_info/', user_views.user_info, name='user_info'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:user_id>/', tracking_views.profile_view, name='user_profile'), 
    path('api/location/<int:user_id>/', tracking_views.get_latest_location, name='get_latest_location'),
    path('forgot-password/', user_views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('verify-otp/', user_views.VerifyOtpView.as_view(), name='verify_otp'),
    path('change-password/', user_views.ChangePasswordView.as_view(), name='change_password'),
]
# from django.urls import path
# from users import views as user_views

# urlpatterns = [
#     path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirect root to login
#     path('admin/', admin.site.urls),
#     path('register/', user_views.RegisterView.as_view(), name='register'),
#     path('login/', user_views.LoginView.as_view(), name='login'),
#     path('dashboard/', user_views.dashboard, name='dashboard'),
    
