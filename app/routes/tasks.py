from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.models.comment import Comment
from app.utils.decorators import admin_required
from app import db
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/')
@login_required
def index():
    if current_user.is_admin():
        tasks = Task.query.order_by(Task.created_at.desc()).all()
    else:
        tasks = Task.query.filter_by(assigned_to=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template('tasks/index.html', tasks=tasks)

@tasks_bp.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    projects = Project.query.all()
    members = User.query.filter_by(role='Team Member').all()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        due_date_str = request.form.get('due_date')
        project_id = request.form.get('project_id')
        assigned_to = request.form.get('assigned_to')
        
        if not all([title, priority, due_date_str, project_id, assigned_to]):
            flash('Missing required fields.', 'danger')
            return redirect(url_for('tasks.create'))
            
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        
        new_task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            project_id=project_id,
            assigned_to=assigned_to,
            created_by=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.index'))
        
    return render_template('tasks/create.html', projects=projects, members=members)

@tasks_bp.route('/<int:task_id>')
@login_required
def view(task_id):
    task = Task.query.get_or_404(task_id)
    if not current_user.is_admin() and task.assigned_to != current_user.id:
        flash('Unauthorized access to this task.', 'danger')
        return redirect(url_for('tasks.index'))
        
    comments = Comment.query.filter_by(task_id=task.id).order_by(Comment.created_at.asc()).all()
    return render_template('tasks/view.html', task=task, comments=comments)

@tasks_bp.route('/<int:task_id>/status', methods=['POST'])
@login_required
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    if not current_user.is_admin() and task.assigned_to != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
        
    status = request.form.get('status') or request.json.get('status')
    if status in ['Pending', 'In Progress', 'Completed']:
        task.status = status
        db.session.commit()
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({'message': 'Status updated'})
        flash('Status updated successfully.', 'success')
    return redirect(url_for('tasks.view', task_id=task_id))

@tasks_bp.route('/<int:task_id>/comment', methods=['POST'])
@login_required
def add_comment(task_id):
    task = Task.query.get_or_404(task_id)
    if not current_user.is_admin() and task.assigned_to != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
        
    content = request.form.get('content')
    if content:
        comment = Comment(content=content, task_id=task.id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added.', 'success')
        
    return redirect(url_for('tasks.view', task_id=task_id))
