👇

📝 Flask To-Do App

A simple Flask-based To-Do application with user authentication (login & register) and task management features.

🚀 Features

🔑 User Registration & Login (with session-based authentication)

➕ Add new tasks

🔄 Toggle task status (Pending → Working → Done)

❌ Delete individual tasks

🗑️ Clear all tasks

🎨 Modern UI with CSS styling

🌙 Dark mode support (toggle button)

⚡ Flash messages for feedback (auto-hide after 5 sec)

📂 Project Structure
To_Do_List/
│── app/
│   ├── __init__.py        # Flask app factory & DB setup
│   ├── models.py          # Database models (User, Task)
│   ├── routes/
│   │   ├── auth.py        # Authentication routes
│   │   └── tasks.py       # Task management routes
│   └── templates/         # HTML templates
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       ├── tasks.html
│       └── no_user.html
│   └── static/
│       └── css/style.css  # Stylesheet
│
│── run.py                 # Entry point
│── create_user.py         # Script to add default admin user
│── README.md              # Project documentation

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app


Create & activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Initialize database

python run.py


(Optional) Create default admin user

python create_user.py

▶️ Usage

Run the app:

python run.py


Open browser and go to:

http://127.0.0.1:5000/

🔑 Default Login (if create_user.py used)
Username: admin
Password: 1234

🖼️ Screenshots

(Add screenshots of Login Page, Register Page, Task Page, Dark Mode here)

🛠️ Tech Stack

Python (Flask)

SQLite (Database)

HTML, CSS (Frontend)

📌 Future Improvements

Add password hashing (done ✅ using Werkzeug)

User-specific task lists

API support (Flask REST API)

Deployment on Heroku/Render

✍️ Author: Shivam Upadhyay
