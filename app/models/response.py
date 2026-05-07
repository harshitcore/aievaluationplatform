from app import db
from datetime import datetime

class AIResponse(db.Model):
    __tablename__ = 'ai_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    evaluation_id = db.Column(db.Integer, db.ForeignKey('evaluations.id'), nullable=False)
    
    model_name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    # Evaluation Scores (1-5)
    score_accuracy = db.Column(db.Integer, nullable=True)
    score_relevance = db.Column(db.Integer, nullable=True)
    score_clarity = db.Column(db.Integer, nullable=True)
    score_completeness = db.Column(db.Integer, nullable=True)
    score_safety = db.Column(db.Integer, nullable=True)
    
    is_best = db.Column(db.Boolean, default=False)
    is_hallucination = db.Column(db.Boolean, default=False)
    feedback = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<AIResponse {self.model_name} for Eval {self.evaluation_id}>'
