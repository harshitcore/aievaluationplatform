# AI Response Evaluation Platform

A lightweight full-stack platform for evaluating and comparing AI-generated responses through structured human feedback workflows inspired by RLHF (Reinforcement Learning from Human Feedback).

---

# 📌 Project Overview

The AI Response Evaluation Platform is designed to simulate how modern AI systems are evaluated by human annotators. The application allows users to:

* Generate multiple AI responses for a prompt
* Compare responses side-by-side
* Evaluate outputs using structured scoring metrics
* Store evaluations and feedback
* Manage projects and evaluator workflows

This project demonstrates practical full-stack development skills using Flask, SQLAlchemy, SQLite/PostgreSQL, authentication systems, REST APIs, and responsive frontend design.

---

# 🚀 Features

## Core Features

* User Authentication & Authorization
* Role-Based Access Control (Admin / Evaluator)
* AI Response Comparison Interface
* Structured Scoring System
* Evaluation Submission Workflow
* Dashboard Analytics
* Project Management
* Persistent Database Storage
* Responsive UI using Bootstrap

## Evaluation Metrics

Responses can be evaluated on:

* Accuracy
* Relevance
* Clarity
* Completeness
* Safety

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Vanilla JavaScript

## Backend

* Python
* Flask
* Flask Blueprints
* Flask-Login
* Flask-SQLAlchemy

## Database

### Development

* SQLite

### Production / Deployment

* PostgreSQL

## Deployment

* Render
* PyInstaller (Optional Desktop Executable)

---

# 📂 Project Structure

```bash
AI-Response-Evaluation/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   └── __init__.py
│
├── migrations/
├── venv/
├── requirements.txt
├── run.py
├── README.md
└── app.db
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/harshitcore/AIEvaluationPlatform.git
cd "AI Response Evaluation"
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python run.py
```

---

## 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

# 🗄️ Database Configuration

## SQLite (Local Development)

The application automatically creates:

```text
app.db
```

when the server starts.

---

## PostgreSQL (Production)

Set environment variable:

```env
DATABASE_URL=postgresql://username:password@host/database
```

Example Flask configuration:

```python
import os

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///app.db'
)
```

---

# 🔐 Authentication System

The platform uses:

* Flask-Login for session management
* Password hashing using Werkzeug
* Role-Based Access Control (RBAC)

### Roles

| Role      | Permissions                        |
| --------- | ---------------------------------- |
| Admin     | Create projects, manage evaluators |
| Evaluator | Evaluate assigned projects         |

---

# 📊 Database Schema

## Users

| Field         | Type    |
| ------------- | ------- |
| id            | Integer |
| username      | String  |
| password_hash | String  |
| role          | String  |

---

## Projects

| Field        | Type        |
| ------------ | ----------- |
| id           | Integer     |
| title        | String      |
| description  | Text        |
| evaluator_id | Foreign Key |

---

## Evaluations

| Field        | Type        |
| ------------ | ----------- |
| id           | Integer     |
| prompt       | Text        |
| project_id   | Foreign Key |
| evaluator_id | Foreign Key |
| status       | String      |

---

## AI Responses

| Field         | Type           |
| ------------- | -------------- |
| id            | Integer        |
| evaluation_id | Foreign Key    |
| model_name    | String         |
| content       | Text           |
| scores        | Integer Fields |
| feedback      | Text           |

---

# 🔄 Application Workflow

```text
User Login
    ↓
Project Selection
    ↓
Prompt Submission
    ↓
Generate AI Responses
    ↓
Side-by-Side Comparison
    ↓
Scoring & Feedback
    ↓
Store Evaluation in Database
    ↓
Dashboard Analytics
```

---

# 🌐 API Endpoints

| Method   | Route              | Description           |
| -------- | ------------------ | --------------------- |
| GET/POST | /login             | User login            |
| GET/POST | /register          | User registration     |
| GET      | /dashboard         | Main dashboard        |
| GET      | /projects          | View projects         |
| POST     | /projects/create   | Create project        |
| POST     | /eval/api/generate | Generate AI responses |
| POST     | /eval/api/submit   | Submit evaluation     |

---

# 🧠 AI Evaluation Concept

This project is inspired by RLHF (Reinforcement Learning from Human Feedback) pipelines used in modern AI systems.

The workflow:

1. AI generates multiple responses
2. Human evaluators compare outputs
3. Responses are scored on multiple dimensions
4. Evaluation data can later be used for fine-tuning AI systems

This application represents a simplified annotation workflow commonly used in AI model evaluation systems.

---

# 🧪 Testing

## Manual Testing Checklist

* User Registration
* Login / Logout
* Role-based access restriction
* Project creation
* AI response generation
* Evaluation submission
* Database persistence
* Dashboard metrics

---

# 🚀 Deployment

## Render Deployment

### Environment Variables

```env
DATABASE_URL=<your-postgresql-url>
SECRET_KEY=<your-secret-key>
```

---

## Build Command

```bash
pip install -r requirements.txt
```

---

## Start Command

```bash
gunicorn run:app
```

---

# 💻 Desktop Executable (Optional)

The application can also be packaged as a Windows executable using PyInstaller.

```bash
pyinstaller --name "AIEvalPlatform" --add-data "app/templates;app/templates" --add-data "app/static;app/static" run.py
```

---

# 📸 Screenshots

## Login Page

*[Add Login Screenshot Here]*

---

## Dashboard

*[Add Dashboard Screenshot Here]*

---

## Evaluation Interface

*[Add Evaluation Screenshot Here]*

---

# 🔮 Future Improvements

* Real OpenAI API integration
* CSV/JSON export support
* Advanced analytics dashboard
* Multiple AI model support
* Real-time collaborative evaluation
* JWT authentication
* Docker deployment
* Background task queues

---

# 📚 Learning Outcomes

This project demonstrates understanding of:

* Full-stack web development
* REST API architecture
* Database design & ORM
* Authentication systems
* Role-Based Access Control
* AI evaluation workflows
* Frontend-backend integration
* Flask application architecture
* Deployment concepts

---

# 👨‍💻 Author

## Harshit Sharma

* Python Developer
* AI & ML Enthusiast
* Full-Stack Learner
* Music Producer & Creative Technologist

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# ⭐ Acknowledgements

* Flask Documentation
* SQLAlchemy Documentation
* Bootstrap Documentation
* OpenAI & RLHF research concepts

---

# 📬 Contact

For collaboration, feedback, or opportunities:

* GitHub: [github.com/harshitcore](https://github.com/harshitcore)
* LinkedIn: *[www.linkedin.com/in/harshit-sharma-381548283]*
* Email: *[harshitsharma.connnect@gmail.com]*
