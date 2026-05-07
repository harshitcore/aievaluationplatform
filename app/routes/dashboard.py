from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.evaluation import Evaluation
from app.models.response import AIResponse

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
@login_required
def index():
    if current_user.is_admin():
        total_projects = Project.query.count()
        total_evals = Evaluation.query.count()
        recent_projects = Project.query.order_by(Project.created_at.desc()).limit(5).all()
        # Avg score approximation for demo
        # In SQLite, avg() requires some raw SQL or func.avg
        # For simplicity in this demo, we will just pass dummy data or count
    else:
        total_projects = Project.query.filter_by(evaluator_id=current_user.id).count()
        total_evals = Evaluation.query.filter_by(evaluator_id=current_user.id).count()
        recent_projects = Project.query.filter_by(evaluator_id=current_user.id).order_by(Project.created_at.desc()).limit(5).all()

    from app import db
    from sqlalchemy.sql import func
    
    # Calculate real average score from the database
    result = db.session.query(func.avg(AIResponse.score_accuracy)).scalar()
    
    if result is not None:
        avg_score = round(result, 1)
    else:
        avg_score = "N/A"

    return render_template('dashboard.html', 
                           total_projects=total_projects, 
                           total_evals=total_evals, 
                           avg_score=avg_score,
                           recent_projects=recent_projects)
