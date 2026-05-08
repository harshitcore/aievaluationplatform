from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
@login_required
def index():
    now = datetime.utcnow()
    
    if current_user.is_admin():
        total_tasks = Task.query.count()
        completed_tasks = Task.query.filter_by(status='Completed').count()
        pending_tasks = Task.query.filter(Task.status.in_(['Pending', 'In Progress'])).count()
        
        # Overdue logic: due_date < now AND status != 'Completed'
        overdue_tasks = Task.query.filter(Task.due_date < now, Task.status != 'Completed').count()
        
        active_projects = Project.query.count()
        team_members = User.query.filter_by(role='Team Member').count()
        recent_tasks = Task.query.order_by(Task.created_at.desc()).limit(5).all()
        
    else:
        total_tasks = Task.query.filter_by(assigned_to=current_user.id).count()
        completed_tasks = Task.query.filter_by(assigned_to=current_user.id, status='Completed').count()
        pending_tasks = Task.query.filter(Task.assigned_to==current_user.id, Task.status.in_(['Pending', 'In Progress'])).count()
        
        overdue_tasks = Task.query.filter(Task.assigned_to==current_user.id, Task.due_date < now, Task.status != 'Completed').count()
        
        active_projects = Project.query.join(Task).filter(Task.assigned_to == current_user.id).distinct().count()
        team_members = 0
        
        recent_tasks = Task.query.filter_by(assigned_to=current_user.id).order_by(Task.created_at.desc()).limit(5).all()

    return render_template('dashboard.html', 
                           total_tasks=total_tasks, 
                           completed_tasks=completed_tasks, 
                           pending_tasks=pending_tasks,
                           overdue_tasks=overdue_tasks,
                           active_projects=active_projects,
                           team_members=team_members,
                           recent_tasks=recent_tasks)
