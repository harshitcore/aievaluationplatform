from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.project import Project
from app.models.evaluation import Evaluation
from app.models.response import AIResponse
from app.services.ai_service import MockAIService
from app import db

eval_bp = Blueprint('eval', __name__, url_prefix='/eval')

@eval_bp.route('/project/<int:project_id>', methods=['GET'])
@login_required
def evaluate_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    # Simple check: evaluators can only see assigned projects
    if not current_user.is_admin() and project.evaluator_id != current_user.id:
        flash('You are not assigned to this project.', 'danger')
        return redirect(url_for('dashboard.index'))
        
    return render_template('evaluation/evaluate.html', project=project)

@eval_bp.route('/api/generate', methods=['POST'])
@login_required
def generate_response():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
        
    # Call the Mock AI Service
    responses = MockAIService.generate_responses(prompt)
    
    return jsonify(responses)

@eval_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_evaluation():
    data = request.get_json()
    
    project_id = data.get('project_id')
    prompt = data.get('prompt')
    responses_data = data.get('responses')  

    if not all([project_id, prompt, responses_data]):
        return jsonify({'error': 'Missing data'}), 400
        
    # Create Evaluation record
    new_eval = Evaluation(
        project_id=project_id,
        evaluator_id=current_user.id,
        prompt=prompt,
        status='Completed'
    )
    db.session.add(new_eval)
    db.session.flush() 
    
    # Create AIResponse records
    for r_data in responses_data:
        ai_resp = AIResponse(
            evaluation_id=new_eval.id,
            model_name=r_data.get('model_name'),
            content=r_data.get('content'),
            score_accuracy=r_data.get('score_accuracy'),
            score_relevance=r_data.get('score_relevance'),
            score_clarity=r_data.get('score_clarity'),
            score_completeness=r_data.get('score_completeness'),
            score_safety=r_data.get('score_safety'),
            is_best=r_data.get('is_best', False),
            is_hallucination=r_data.get('is_hallucination', False),
            feedback=r_data.get('feedback', '')
        )
        db.session.add(ai_resp)
        
    db.session.commit()
    
    return jsonify({'message': 'Evaluation submitted successfully!'})
