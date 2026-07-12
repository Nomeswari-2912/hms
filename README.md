# Hospital Management System (HMS)

A comprehensive Django-based web application for managing hospital operations including patient records, doctor schedules, appointments, billing, and pharmacy inventory.

## Project Structure

```
hms/
├── accounts/                          # User authentication & account management
│   ├── models.py                     # User account models
│   ├── views.py                      # Account views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Account forms
│   └── templates/accounts/           # Account templates
│
├── patients/                          # Patient management module
│   ├── models.py                     # Patient models
│   ├── views.py                      # Patient views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Patient forms
│   └── templates/patients/           # Patient templates
│
├── doctors/                           # Doctor management module
│   ├── models.py                     # Doctor models
│   ├── views.py                      # Doctor views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Doctor forms
│   └── templates/doctors/            # Doctor templates
│
├── appointments/                      # Appointment scheduling module
│   ├── models.py                     # Appointment models
│   ├── views.py                      # Appointment views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Appointment forms
│   └── templates/appointments/       # Appointment templates
│
├── billing/                           # Billing & payments module
│   ├── models.py                     # Billing models
│   ├── views.py                      # Billing views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Billing forms
│   └── templates/billing/            # Billing templates
│
├── pharmacy/                          # Pharmacy inventory module
│   ├── models.py                     # Pharmacy models
│   ├── views.py                      # Pharmacy views
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Pharmacy forms
│   └── templates/pharmacy/           # Pharmacy templates
│
├── hospital_management_system/        # Main project configuration
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Main URL routing
│   ├── wsgi.py                       # WSGI configuration
│   └── asgi.py                       # ASGI configuration
│
├── templates/                         # Global templates
│   ├── base.html                     # Base template
│   ├── home.html                     # Home page
│   └── accounts/register.html        # Registration template
│
├── static/                            # Static files (CSS, JS, images)
├── media/                             # User uploaded media files
├── manage.py                          # Django management script
└── db.sqlite3                         # SQLite database
```

## Features

- **Patient Management**: Register and manage patient information
- **Doctor Management**: Maintain doctor profiles and schedules
- **Appointment Scheduling**: Book and manage patient appointments
- **Billing System**: Generate and track bills
- **Pharmacy Management**: Manage medicine inventory

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (included with Python)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nomeswari-2912/hms.git
   cd hms
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Main Modules

- **Accounts**: User registration and authentication
- **Patients**: View and manage patient records
- **Doctors**: Manage doctor information and availability
- **Appointments**: Schedule and track appointments
- **Billing**: Generate invoices and track payments
- **Pharmacy**: Manage medicine inventory and prescriptions

## Project Configuration

Key settings are located in `hospital_management_system/settings.py`:
- Database configuration
- Installed apps
- Static files location
- Template directories
- Time zone and language settings

## Database Models

The application uses Django ORM with SQLite database. Models are defined in each module's `models.py` file for:
- User accounts
- Patient information
- Doctor profiles
- Appointments
- Billing records
- Pharmacy inventory

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is open source and available under the MIT License.

## Author

Nomeswari-2912

## Contact

For questions or issues, please open an issue on GitHub.
