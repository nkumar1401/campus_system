# Campus  System

## Overview
The **Campus  System** is a web-based application designed to streamline and manage the admissions process of an educational institute. It provides a centralized platform for students, administrators, and faculty to interact efficiently. The system is built using **Django** for the backend and **MySQL** as the database.

## Features
- **Student Registration & Admission**: New students can apply for admission online.
- **Admin Dashboard**: Manage student records, applications, and admissions.
- **Authentication & Authorization**: Secure access for students and admins.
- **Application Tracking**: Students can check the status of their application.
- **User Roles**: Different levels of access for students, faculty, and administrators.
- **Email Notifications**: Automated emails for admission updates.

## Technologies Used
- **Backend**: Django
- **Database**: MySQL
- **Authentication**: Django Authentication System
- **Other Tools**: Docker (optional), Celery for async tasks (optional)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (3.x)
- MySQL
- Django

### Backend Setup (Django)
```sh
# Clone the repository
git clone https://github.com/yourusername/campus-system.git
cd campus-system

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database settings in settings.py

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

## Contribution Guidelines
- Fork the repository and create a new branch for your feature.
- Follow proper coding standards and best practices.
- Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License.

## Contact
For any queries or suggestions, feel free to reach out at [nkbhagatkar@gmail.com].

