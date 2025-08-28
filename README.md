# 🌍 TravelLykke - Travel Booking Platform

**TravelLykke** is a comprehensive travel booking web application built with Django and MySQL, designed to provide seamless travel booking experiences for users while offering administrative capabilities for travel operators.

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Development Process](#-development-process)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🔐 User Authentication
- **User Registration**: New users can create accounts with username and password
- **User Login/Logout**: Secure authentication system with session management
- **Profile Management**: Users can update their personal information (name, email, phone)

### 🎫 Travel Booking System
- **Browse Travel Options**: View available flights, trains, and buses
- **Advanced Search**: Filter by source, destination, and date
- **Real-time Booking**: Book travel with seat selection and automatic availability updates
- **Booking Management**: View, track, and cancel existing bookings

### 👨‍💼 Administrative Features
- **Admin Dashboard**: Comprehensive control panel for travel operators
- **Travel Option Management**: Add new travel options (flights, trains, buses)
- **Booking Overview**: Monitor all bookings and customer activity

### 🎨 User Experience
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Intuitive Navigation**: Clean, professional UI with accessibility features
- **Real-time Feedback**: Instant success/error messages for user actions
- **Professional Branding**: Consistent design language with TravelLykke branding

## 🛠 Technology Stack

### Backend
- **Framework**: Django 5.2.5
- **Language**: Python 3.13.5
- **Database**: MySQL 8.0
- **Authentication**: Django's built-in authentication system
- **ORM**: Django ORM for database operations

### Frontend
- **Framework**: Bootstrap 5
- **Templating**: Django Templates
- **Styling**: Custom CSS with responsive design
- **Icons**: Bootstrap Icons
- **JavaScript**: Vanilla JS for interactivity

### Development Tools
- **Version Control**: Git & GitHub
- **Database Client**: MySQL Connector/Python
- **Static Files**: Django's collectstatic for production
- **Development Server**: Django development server

## 📁 Project Structure

```
TravelLykke/
├── 📄 README.md                 # Project documentation
├── 📄 requirements.txt          # Python dependencies
├── 📄 .gitignore               # Git ignore rules
├── 📄 .env.example             # Environment variables template
├── 📄 DEPLOYMENT.md            # Deployment instructions
├── 📁 backend/                 # Django backend
│   ├── 📄 manage.py            # Django management script
│   ├── 📁 travel_booking/      # Main Django project
│   │   ├── 📄 __init__.py
│   │   ├── 📄 settings.py      # Django configuration
│   │   ├── 📄 urls.py          # Main URL routing
│   │   ├── 📄 wsgi.py          # WSGI configuration
│   │   └── 📄 asgi.py          # ASGI configuration
│   ├── 📁 core/               # Main application
│   │   ├── 📄 __init__.py
│   │   ├── 📄 models.py        # Database models
│   │   ├── 📄 views.py         # Application logic
│   │   ├── 📄 urls.py          # App URL routing
│   │   ├── 📄 admin.py         # Admin interface
│   │   ├── 📄 apps.py          # App configuration
│   │   ├── 📄 tests.py         # Unit tests
│   │   └── 📁 migrations/      # Database migrations
│   └── 📁 staticfiles/         # Collected static files
├── 📁 frontend/               # Frontend assets
│   ├── 📁 static/             # Static files
│   │   └── 📁 css/
│   │       └── 📄 style.css    # Custom styles
│   └── 📁 templates/          # HTML templates
│       ├── 📄 base.html        # Base template
│       ├── 📄 home.html        # Homepage
│       ├── 📄 login.html       # Login page
│       ├── 📄 register.html    # Registration page
│       ├── 📄 profile.html     # User profile
│       ├── 📄 travel_options.html # Travel search
│       ├── 📄 book_travel.html # Booking page
│       ├── 📄 my_bookings.html # User bookings
│       ├── 📄 cancel_booking.html # Cancel booking
│       ├── 📄 admin_dashboard.html # Admin panel
│       ├── 📄 add_travel_option.html # Add travel
│       ├── 📄 404.html         # Error page
│       └── 📄 500.html         # Server error page
└── 📁 config/                 # Configuration files
    └── 📄 database.sql         # Database schema
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+ (Recommended: 3.13.5)
- MySQL 8.0+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/saiteja7065/TravelLykke.git
cd TravelLykke
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv backend/venv

# Activate virtual environment
# On Windows:
backend\venv\Scripts\activate
# On macOS/Linux:
source backend/venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE travel_booking_db;
EXIT;

# Configure database in backend/travel_booking/settings.py
# Update DATABASES configuration with your MySQL credentials
```

### 5. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
# Add your database credentials and secret key
```

### 6. Run Migrations
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 9. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 🎯 Usage

### For End Users

1. **Registration**: Create a new account on the registration page
2. **Login**: Sign in with your credentials
3. **Browse Travel**: Search for travel options by source, destination, and date
4. **Book Travel**: Select your preferred option and book seats
5. **Manage Bookings**: View and cancel your bookings from the profile area
6. **Profile**: Update your personal information

### For Administrators

1. **Admin Login**: Sign in with staff/superuser credentials
2. **Access Dashboard**: Navigate to admin dashboard for management features
3. **Add Travel Options**: Create new flights, trains, or bus routes
4. **Monitor Bookings**: Track all customer bookings and activities

## 🔗 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/` | Homepage | No |
| GET/POST | `/register/` | User registration | No |
| GET/POST | `/login/` | User login | No |
| GET | `/logout/` | User logout | Yes |
| GET | `/travel-options/` | Browse travel options | No |
| GET/POST | `/book/<int:travel_id>/` | Book travel | Yes |
| GET | `/my-bookings/` | User's bookings | Yes |
| GET/POST | `/cancel-booking/<int:booking_id>/` | Cancel booking | Yes |
| GET/POST | `/profile/` | User profile | Yes |
| GET | `/admin-dashboard/` | Admin dashboard | Staff |
| GET/POST | `/add-travel-option/` | Add travel option | Staff |

## 🔨 Development Process

### Architecture Decisions

1. **MVC Pattern**: Implemented using Django's MVT (Model-View-Template) architecture
2. **Database Design**: Normalized schema with proper relationships between users, bookings, and travel options
3. **Authentication**: Leveraged Django's built-in authentication system for security
4. **Frontend**: Bootstrap-based responsive design for cross-device compatibility

### Key Models

```python
# User Profile Extension
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

# Travel Options
class TravelOption(models.Model):
    type = models.CharField(max_length=50)  # Flight, Train, Bus
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

# Booking System
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=True)
```

### Security Features

- **CSRF Protection**: Enabled for all forms
- **SQL Injection Prevention**: Using Django ORM
- **User Authentication**: Session-based authentication
- **Permission Control**: Staff-only access for admin features
- **Input Validation**: Server-side validation for all user inputs

## 🌐 Deployment

### Production Requirements

1. **Web Server**: Gunicorn + Nginx
2. **Database**: MySQL 8.0+ (production instance)
3. **Static Files**: Collected and served by Nginx
4. **Environment**: Python 3.8+ virtual environment

### Deployment Platforms

- **PythonAnywhere**: Ready for deployment with MySQL support
- **AWS EC2**: Scalable cloud deployment
- **Heroku**: Quick deployment with PostgreSQL addon
- **DigitalOcean**: VPS deployment with full control

### Environment Variables

```bash
# Production settings
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=mysql://user:password@host:port/database
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write unit tests for new features

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Sai Teja**
- GitHub: [@saiteja7065](https://github.com/saiteja7065)
- Project: TravelLykke Travel Booking Platform

---

## 🙏 Acknowledgments

- **Django Documentation**: For comprehensive framework guidance
- **Bootstrap Team**: For the responsive CSS framework
- **MySQL**: For reliable database management
- **Travel Industry**: For inspiration and requirements understanding

---

**TravelLykke** - Making travel booking simple, efficient, and enjoyable! 🌍✈️🚂🚌
