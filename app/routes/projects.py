from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.project import Project
from app.utils.decorators import admin_required
from app import db

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
@login_required
def index():
    if current_user.is_admin():
        projects = Project.query.all()
    else:
        # Team Members see projects where they have assigned tasks
        from app.models.task import Task
        projects = Project.query.join(Task).filter(Task.assigned_to == current_user.id).distinct().all()
    return render_template('projects/index.html', projects=projects)

@projects_bp.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        new_project = Project(title=title, description=description, created_by=current_user.id)
        db.session.add(new_project)
        db.session.commit()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('projects.index'))
        
    return render_template('projects/create.html')
