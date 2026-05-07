# AI Response Evaluation Platform

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.12+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey.svg)

## Project Overview
The AI Response Evaluation Platform is a full-stack, production-ready web application built to simulate the complex evaluation workflows used in **RLHF** (Reinforcement Learning from Human Feedback) and **SFT** (Supervised Fine-Tuning) pipelines. 

It provides a structured, highly professional environment for Human Evaluators to prompt large language models, view side-by-side responses, and score them based on specific qualitative criteria to generate preference data.



## Core Features
- **Real OpenAI Integration**: Direct integration with the `openai` Python SDK to generate live, side-by-side responses from multiple models. (Easily toggleable to a Mock API for offline demonstrations).
- **Role-Based Access Control (RBAC)**: Secure, segmented workflows. Admins have global visibility and project creation rights, while Evaluators only see tasks explicitly assigned to them.
- **Structured RLHF Scoring**: Evaluators grade responses on Accuracy, Relevance, Clarity, Completeness, and Safety (1-5 scale) and identify model "Hallucinations".
- **Database Integrity**: Uses SQLAlchemy ORM with transactional sessions (`flush` and `commit`) to guarantee data integrity across highly relational data.
- **SaaS Deployment Ready**: Built to be deployed to the cloud (Render/PostgreSQL) or instantly packaged as a standalone, double-clickable Windows `.exe` application.

## Documentation Suite
This project includes a comprehensive set of technical guides located in the `docs/` folder:

1. **[UNDERSTANDING.md](docs/UNDERSTANDING.md)**: The ultimate Technical Interview Cheat Sheet. Explains the architecture, the Application Factory pattern, database transaction tricks, and anticipated interview questions.
2. **[stepsN.md](docs/stepsN.md)**: A complete, actionable guide to managing the database, from SQLite configuration to Flask-Migrate schema changes.
3. **[Render Deployment.md](docs/Render Deployment.md)**: Step-by-step roadmap to deploying the app to the internet with Gunicorn and a Cloud PostgreSQL cluster.
4. **[GitHub update.md](docs/GitHub%20update.md)**: Documentation on hosting the `.exe` via GitHub Releases and implementing seamless in-app auto-updates.
5. **[TEST.txt](docs/TEST.txt)**: A strict quality assurance roadmap and edge-case debugging guide.

 

## Architecture & Tech Stack
- **Frontend**: HTML5, Vanilla JavaScript (ES6), CSS, Bootstrap 5.
- **Backend**: Python 3, Flask (Application Factory architecture).
- **Database**: SQLite (Local) / PostgreSQL (Cloud) with SQLAlchemy ORM.
- **Authentication**: Flask-Login (session-based cookies) with Werkzeug password hashing.
- **Packaging**: PyInstaller (for standalone executables).

 

## Setup & Run Instructions

### Option 1: Standard Python Execution
1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd "AI Response Evaluation"
   ```
2. **Setup the Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure your API Key**:
   Create a `.env` file in the root directory and add:
   ```env
   OPENAI_API_KEY=sk-your-api-key-here
   ```
5. **Run the server**:
   ```bash
   python run.py
   ```
   *The application will automatically generate the `app.db` file and open your default web browser.*

### Option 2: Running the Executable (.exe)
If you have packaged the application (or received the `dist/` folder):
1. Navigate to the `dist` folder.
2. Double-click `AIEvalPlatform.exe`. 
3. The background server will boot silently, and your browser will automatically launch the application.

 

## Why This Project Matters
This application captures the core mechanics of an internal AI annotation tool. In modern AI development, human labelers are presented with multiple model outputs and asked to grade them on specific axes (helpfulness, safety, accuracy). This data is the lifeblood required to construct reward models for **PPO (Proximal Policy Optimization)**. This application demonstrates a profound understanding of that exact pipeline, merging data science workflows with full-stack engineering.
