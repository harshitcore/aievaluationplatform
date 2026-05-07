from app import db
from datetime import datetime

class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    evaluator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    prompt = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending') # 'Pending', 'Completed'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    responses = db.relationship('AIResponse', backref='evaluation', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Evaluation {self.id} for Project {self.project_id}>'
