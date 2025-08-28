📝 To-Do List Application
A modern, feature-rich web application for managing your daily tasks efficiently. Built with Flask and SQLAlchemy, this app provides a seamless task management experience with user authentication and a beautiful responsive interface.

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Flask-2.0%252B-green
https://img.shields.io/badge/SQLite-Database-lightgrey
https://img.shields.io/badge/Design-Responsive-orange

✨ Key Features
🔐 Secure Authentication System
User registration with secure password hashing

Login/logout functionality with session management

Protected routes - only authenticated users can access tasks

Automatic redirect to login page for unauthorized access

📝 Comprehensive Task Management
Add Tasks: Quick and easy task creation

Track Progress: Three status levels - Pending, Working, Done

Visual Status Indicators: Color-coded badges for easy identification

Task Actions:

Toggle between status states with "Next" button

Delete individual tasks

Clear all tasks at once

Real-time Updates: Immediate feedback for all operations

🎨 Modern User Interface
Dark/Light Mode: Toggle between themes with persistent preferences

Responsive Design: Works perfectly on desktop, tablet, and mobile devices

Smooth Animations: Beautiful transitions and hover effects

Modern Color Scheme: Professional indigo and purple gradient theme

Intuitive Navigation: Clean and user-friendly interface

🔒 Security & Reliability
Password hashing with Werkzeug security

SQL injection prevention through SQLAlchemy ORM

Session-based authentication

Input validation and error handling

🛠️ Technology Stack
Backend Framework: Flask (Python)

Database: SQLite with SQLAlchemy ORM

Frontend: HTML5, CSS3, Vanilla JavaScript

Authentication: Werkzeug security utilities

Styling: Custom CSS with CSS variables for theming

Database ORM: SQLAlchemy

📋 Prerequisites
Before running this application, ensure you have:

Python 3.8 or higher installed

pip (Python package manager)

Modern web browser (Chrome, Firefox, Safari, or Edge)

📖 How to Use
First Time Setup
Register a New Account: Click on "Register" in the navigation menu

Create Credentials: Choose a username and password

Login: Use your credentials to access the application

Managing Tasks
Add a Task:

Type your task in the input field at the top

Click "Add" button or press Enter

Update Task Status:

Click "Next" button to cycle through statuses: Pending → Working → Done

Visual badges show current status with color coding

Delete Tasks:

Click "Delete" button next to any task to remove it

Use "Clear All Tasks" button to remove all tasks at once

Theme Switching:

Click the moon/sun icon in the header to toggle between dark and light modes

Your preference is saved automatically

🗂️ Project Structure

todo-app/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── models.py            # Database models (User, Task)
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   └── tasks.py         # Task management routes
│   └── templates/           # HTML templates
│       ├── base.html        # Base template with navigation
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── tasks.html       # Main tasks page
│       └── no_user.html     # Error page for non-existent users
├── static/
│   └── css/
│       └── style.css        # Main stylesheet
├── instance/
│   └── todo.db             # SQLite database (auto-created)
├── requirements.txt         # Python dependencies
├── run.py                  # Application entry point
└── README.md               # This file

🔧 Customization
Changing Color Theme
Edit the CSS variables in static/css/style.css:

css
:root {
    --primary-color: #6366F1;    /* Main theme color */
    --secondary-color: #8B5CF6;  /* Secondary color */
    /* Add more custom colors as needed */
}

Modifying Database
The application uses SQLite by default. To change database configuration, edit app/__init__.py:

python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'


🌟 Future Enhancements
Potential features for future versions:

Task categories and tags

Due dates and reminders

Task prioritization

Data export functionality

Email notifications

Collaborative task sharing

🤝 Contributing
Contributions are welcome! Feel free to:

1.Fork the project

2.Create a feature branch

3.Make your changes

4.Submit a pull request

📄 License
This project is open source and available under the MIT License.

📞 Support
If you encounter any issues or have questions:

Check the troubleshooting section above

Ensure all dependencies are properly installed

Verify your Python version is 3.8+
