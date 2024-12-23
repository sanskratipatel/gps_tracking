# accounts/utils.py

import random
from django.core.cache import cache

def send_otp(email):
    otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP
    cache.set(email, otp, timeout=300)  # Store OTP in cache for 5 minutes
    # Send the OTP to the user's email (implement your email sending logic here)
    print(f"OTP sent to {email}: {otp}")  # Debugging output