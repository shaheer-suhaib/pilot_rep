<img width="487" height="356" alt="image" src="https://github.com/user-attachments/assets/8ff0c610-f3e8-4e87-a216-e9cc25601264" /># Pilot Logbook Management System

A comprehensive Django REST API application designed for aviation flight logging and management. This system enables pilots to record flight details while providing checkers with tools to review and validate flight logs.

## Project Overview

![alt text](thumbnail.PNG)

<img width="242" height="329" alt="image" src="https://github.com/user-attachments/assets/85b93860-7f9d-49d5-a8c0-104b7edb83e7" />

<img width="477" height="356" alt="image" src="https://github.com/user-attachments/assets/603f0109-a4ae-4aeb-92c6-4a7b3c2d3e91" />



This aviation management platform delivers:

- **Dual User Authentication**: Separate registration and login systems for pilots and checkers
- **Comprehensive Flight Logging**: Detailed flight record creation with aircraft, route, and crew information
- **Flight Record Review**: Checker dashboard for reviewing and marking flight submissions
- **Advanced Filtering**: Query flight logs by pilot, route, and review status
- **RESTful API Architecture**: Clean API endpoints for frontend integration

## Database Architecture

![alt text](DataBase-tables.png)

### Core Models

**User Model** (Custom Authentication)

- Primary identifier (ID)
- Email address (unique)
- username
- password

**Pilot Model**

- Extends user with pilot-specific attributes

**Checker Model**

- Extends user with checker-specific attributes

**Aircraft Model**

- Aircraft type designation
- Tail number identifier

**FlightCategory Model**

- Engine classification
- Role assignment
- Mission type

**FlightLog Model**

- Flight date and duration
- Route information
- Crew members (PIC and Co-Pilot)
- Departure and arrival timestamps
- Flight conditions (IFR/VFR, Day/Night)
- Review status flag
- Foreign keys to Pilot, Aircraft, and Category

## Technology Stack

- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Deployment**: Railway Platform

## Prerequisites

Ensure your development environment includes:

- Python 3.8 or higher
- PostgreSQL database instance
- pip package manager
- Virtual environment tool (venv/virtualenv)

## Installation Instructions





### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd pilotlogbook
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```plaintext
DJANGO_SECRET_KEY=your_django_secret_key_here
DJANGO_DEBUG=True
DATABASE_URL=postgresql://username:password@host:port/database_name
```

### 5. Database Setup

Execute migrations to initialize database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

For admin panel access:

```bash
python manage.py createsuperuser
```

### 7. Launch Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## API Endpoints Documentation

### User Registration

**Pilot Registration**

```http
POST /api/new_user/pilot_sub/
Content-Type: application/json

{
  "id": 12345,
  "email": "pilot@example.com",
  "name": "John Doe",
  "password": "secure_password"
}
```

**Checker Registration**

```http
POST /api/new_user/checker_sub/
Content-Type: application/json

{
  "id": 67890,
  "email": "checker@example.com",
  "name": "Jane Smith",
  "password": "secure_password"
}
```

### Authentication

**Pilot Login**

```http
POST /api/login/pilot/
Content-Type: application/json

{
  "email": "pilot@example.com",
  "password": "secure_password"
}
```

**Checker Login**

```http
POST /api/login/checker/
Content-Type: application/json

{
  "email": "checker@example.com",
  "password": "secure_password"
}
```

### Flight Log Operations

**Create Flight Log**

```http
POST /api/new_user/today_data/FlightLog/{user_id}/
Content-Type: application/json

{
  "date": "2025-01-15",
  "route": "ISB-LHE",
  "Additional_note": "Clear weather conditions",
  "duration": 120,
  "Pilot_in_comm": "Capt. John",
  "Co_Pilot": "FO. Mike",
  "Take_off_time": "2025-01-15T08:00:00Z",
  "Landing_time": "2025-01-15T10:00:00Z",
  "Instrument_Flu": "IFR",
  "Day_night": "Day",
  "typee": "Boeing 737",
  "tail_no": "AP-BEG",
  "engine": "Jet",
  "role": "Captain",
  "mission": "Passenger"
}
```

**Retrieve Flight Logs**

```http
GET /api/checker/today_data/get_data/
GET /api/checker/today_data/get_data/?read=false
```

**Filter Flight Logs**

```http
GET /api/checker/filter/?pilot_id=12345
GET /api/checker/filter/?route=ISB-LHE
GET /api/checker/filter/?All_pilot=true
```

**Mark Flight as Reviewed**

```http
PUT /api/checker/apply_marked/{mission_id}
```

**Get Marked Flights**

```http
GET /api/checker/get_marked/
```

## Deployment Configuration

### Railway Platform Deployment

The application includes a `Procfile` for Railway deployment:

### Required Environment Variables

Configure these on your hosting platform:

- `DJANGO_SECRET_KEY`: Django security key
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Authorized domain names

## CORS Configuration

The application permits cross-origin requests for frontend integration:

```python
CORS_ALLOW_ALL_ORIGINS = True  # Configure specific origins in production
```

## Project Structure

```
pilotlogbook/
├── logbook2/              # Main application module
│   ├── models.py          # Database models
│   ├── views.py           # API view logic
│   ├── serializer.py      # DRF serializers
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   └── migrations/        # Database migrations
├── pilotlogbook/          # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI entry point
│   └── asgi.py            # ASGI entry point
├── manage.py              # Django management script
├── Procfile               # Deployment configuration
├── .gitignore             # Git exclusions
└── requirements.txt       # Python dependencies
```
