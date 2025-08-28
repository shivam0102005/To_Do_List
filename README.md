# 🚀 To-Do List Application

A modern, responsive, and user-friendly To-Do List web application built with Flask and SQLAlchemy. Features user authentication, task management, and a beautiful dark/light mode interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Responsive](https://img.shields.io/badge/Design-Responsive-orange)

## ✨ Features

### 🔐 User Authentication
- User registration and login system
- Secure password hashing with Werkzeug
- Session management
- Protected routes

### 📝 Task Management
- Add new tasks with simple form
- Toggle task status (Pending → Working → Done)
- Delete individual tasks
- Clear all tasks at once
- Visual status badges with colors

### 🎨 Modern UI/UX
- Clean, responsive design
- Dark/Light mode toggle
- Smooth animations and transitions
- Gradient backgrounds and modern colors
- Mobile-friendly interface

### 🔒 Security Features
- Password hashing and salting
- SQL injection prevention
- Session protection
- Input validation

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Werkzeug security
- **Styling**: Custom CSS with CSS variables

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python run.py
Access the application
Open your browser and go to http://localhost:5000

📁 Project Structure
todo-app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models (User, Task)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes
│   │   └── tasks.py         # Task management routes
│   └── templates/
│       ├── base.html        # Base template
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── tasks.html       # Main tasks page
│       └── no_user.html     # Error page for non-existent users
├── static/
│   └── css/
│       └── style.css        # Main stylesheet
├── instance/
│   └── todo.db             # SQLite database (created automatically)
├── requirements.txt         # Python dependencies
├── run.py                  # Application entry point
└── README.md              # This file
🚀 Usage
Register a new account or login with existing credentials

Add tasks using the input field at the top

Toggle task status by clicking "Next" button

Delete tasks individually or clear all at once

Switch between dark/light mode using the moon/sun button

Logout when done

🎯 Key Features in Detail
User Authentication
Secure registration with password hashing

Session-based login system

Automatic redirect to login for protected routes

Custom error pages for non-existent users

Task Management
Three status states: Pending (yellow), Working (blue), Done (green)

Visual indicators: Color-coded badges for quick status recognition

One-click actions: Simple buttons for all operations

Real-time updates: Immediate feedback for all actions

Responsive Design
Works perfectly on desktop, tablet, and mobile devices

Flexible layout that adapts to screen size

Touch-friendly buttons and forms

Dark/Light Mode
Toggle between themes with persistent preference

Smooth transitions between modes

System-appropriate default styling

🔧 Configuration
The application uses the following configuration:

Secret Key: Used for session security

Database: SQLite with file-based storage

Debug Mode: Enabled for development

To modify configuration, edit the create_app() function in app/__init__.py.

🐛 Troubleshooting
Common Issues
Port already in use

bash
# Kill the process using port 5000
lsof -ti:5000 | xargs kill
Database issues

bash
# Delete the database file and restart
rm instance/todo.db
Dependency issues

bash
# Reinstall requirements
pip install -r requirements.txt
Debug Mode
For development, debug mode is enabled. In production, make sure to:

Set debug=False

Use a proper WSGI server (Gunicorn, uWSGI)

Set a strong SECRET_KEY

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Flask community for excellent documentation

SQLAlchemy for robust ORM capabilities

Modern CSS techniques for beautiful UI
