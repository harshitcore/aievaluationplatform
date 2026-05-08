# 📌 Team Task Management Platform

A polished, full-stack web application designed for collaborative team workflow. This platform allows administrators to create projects, assign tasks to team members, track statuses, and monitor overdue tasks through an intuitive dashboard.

## 🚀 Key Features

* **User Authentication**: Secure Signup/Login using Flask-Login and password hashing.
* **Role-Based Access Control (RBAC)**: Distinct permissions for `Admin` and `Team Member`.
* **Project & Team Management**: Admins can structure work into separate projects.
* **Task Assignment & Tracking**: Create tasks with priorities (Low, Medium, High) and deadlines.
* **Overdue Task Monitoring**: Dynamic dashboard automatically flags tasks that have passed their due date and remain incomplete.
* **Interactive Dashboard**: Visual metrics showing Total, Pending, Completed, and Overdue tasks.
* **Responsive UI**: Built with Bootstrap 5 for a clean, modern interface.

## 🛠️ Tech Stack

* **Backend**: Python, Flask, Flask-Login, Flask-SQLAlchemy
* **Frontend**: HTML5, Bootstrap 5, Vanilla JavaScript
* **Database**: SQLite (Local), PostgreSQL (Production)
* **Deployment Readiness**: Configured for Railway with `Procfile` and environment variable handling.

## ⚙️ Installation & Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/TeamTaskManager.git
   cd TeamTaskManager
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python run.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## 🗄️ Database Configuration
The application automatically creates an `app.db` SQLite database for local development when the server starts. For production, set the `DATABASE_URL` environment variable to your PostgreSQL connection string.

## 📂 Documentation
For deeper insights into the project, refer to the documentation artifacts:
- [IMPLEMENTATION.md](docs/IMPLEMENTATION.md)
- [UNDERSTANDING.md](docs/UNDERSTANDING.md)
- [DEPLOYMENT.md](docs/DEPLOYMENT.md)
