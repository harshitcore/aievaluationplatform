from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.user import User
from app.utils.decorators import admin_required
from app import db

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
@login_required
def index():
    if current_user.is_admin():
        projects = Project.query.all()
    else:
        projects = Project.query.filter_by(evaluator_id=current_user.id).all()
    return render_template('projects/index.html', projects=projects)

@projects_bp.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    evaluators = User.query.filter_by(role='Evaluator').all()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        evaluator_id = request.form.get('evaluator_id')
        
        # evaluator_id could be empty
        eval_id = int(evaluator_id) if evaluator_id else None
        
        new_project = Project(title=title, description=description, evaluator_id=eval_id)
        db.session.add(new_project)
        db.session.commit()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('projects.index'))
        
    return render_template('projects/create.html', evaluators=evaluators)
