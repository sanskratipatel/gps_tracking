# **Live Location Tracking System**
ghgg
A real-time location tracking system built using **Python**, **Django** and **WebSockets**. This system provides features like user authentication, live location updates, admin controls, and role-based access. The project uses PostgreSQL as the database and integrates OpenCage for reverse geocoding to enhance location data.


## **Features**

1. **User Management**  
   - User registration and login with JWT-based authentication.  
   - Role-based access control (admin and normal users).  
   - Password recovery: Forgot Password, Change Password functionalities.

2. **Real-Time Location Tracking**  
   - WebSocket-based updates every 3 seconds.  
   - Map integration using Leaflet.js for real-time location display.  
   - Reverse geocoding using the OpenCage API (via `geopy` library).

3. **Admin Dashboard**  
   - View live locations of all users.  
   - Manage user roles and data.  

4. **Database**  hhh
   - PostgreSQL database to store user data and location logs.

5. **Responsive Frontend**  
   - User-friendly HTML templates with integrated CSS and JavaScript.
dddf
---

## **Technologies Used**

- **Backend**: Django, Django Rest Framework (DRF), Django Channels  
- **Frontend**: HTML, CSS, JavaScript (Leaflet.js for map rendering)  
- **Database**: PostgreSQL  
- **Real-Time Updates**: Django Channels, WebSockets  
- **Geocoding**: OpenCage API with `geopy`  

---

## **Project Structure**

```plaintext
live_location_tracking/
├── live_location_tracking/          # Main project folder
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # URL routing
│   ├── asgi.py                      # ASGI configuration (WebSockets)
│   ├── wsgi.py                      # WSGI configuration (for production)
│   ├── routing.py                   # WebSocket routing
├── users/                           # User management app
│   ├── models.py                    # User model with custom fields
│   ├── views.py                     # Views for registration, login, password reset
│   ├── serializers.py               # Serializers for user data
│   ├── templates/                   # User-related templates
│   │   ├── forget_password.html
│   │   ├── change_password.html
│   │   ├── verify_password.html
├── tracking/                        # Location tracking app
│   ├── models.py                    # Models for storing user location logs
│   ├── consumers.py                 # WebSocket consumers for live updates
│   ├── serializers.py               # Serializers for location data
│   ├── templates/                   # Templates for tracking
│   │   ├── map.html                 # Map view for live tracking
├── templates/                       # Common templates
│   ├── base.html                    # Common layout
│   ├── login.html                   # Login page
│   ├── register.html                # Registration page
│   ├── dashboard.html               # Admin dashboard
├── static/                          # Static files (CSS, JS, Images)
├── manage.py                        # Django management script
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

---

## **Setup Guide**

### Prerequisites

- Python 3.8 or higher  
- PostgreSQL installed and running  


### Installation Steps

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/live-location-tracking.git
   cd live-location-tracking
   ```

2. **Create and Activate Virtual Environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**  
   - Create a PostgreSQL database named `live_location_tracking`.  
   - Update the `DATABASES` setting in `live_location_tracking/settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'live_location_tracking',
             'USER': '<your-db-username>',
             'PASSWORD': '<your-db-password>',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**  
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
   - User Interface: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **Usage**

1. **User Registration and Login**
   - Register a new user account using the registration form.
   - Login using your credentials to access the map and dashboard.

2. **Live Location Updates**
   - Update locations every 3 seconds (simulated in the project).
   - View live locations on the map in real time.

3. **Password Recovery**
   - Request a password reset via email.
   - Follow the link to change your password.

---



## **Technologies Used**

- **Frontend**: HTML5, CSS3, JavaScript, Leaflet.js  
- **Backend**: Django, Django Channels  
- **Database**: PostgreSQL  
- **Real-Time Features**: WebSockets  

---

## **API Endpoints**

### **User Authentication**
- **POST** `/api/register/`  
  Register a new user.  
- **POST** `/api/login/`  
  Authenticate user and generate JWT.  
- **POST** `/api/forget-password/`  
  Request password reset.  
- **POST** `/api/change-password/`  
  Change password with verification.

### **Tracking**
- **POST** `/api/update-location/`  
  Update the user’s live location.  
- **GET** `/api/location-history/`  
  Retrieve location history for the user.  
- **GET** `/api/dashboard/`  
  Admin view of all users’ locations.  

---

## **Dependencies**

The project’s dependencies are listed in `requirements.txt`:

```plaintext
Django==4.2
djangorestframework==3.14
channels==4.0
channels-redis==4.0
Pillow==9.1.0
PyJWT==2.6
geopy==2.2.0
psycopg2==2.9.6
leaflet==1.7.1
```

---

## **Contribution**

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to let me know if you want adjustments or additional details!
