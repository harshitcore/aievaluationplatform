from app import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    evaluator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    evaluations = db.relationship('Evaluation', backref='project', lazy='dynamic')

    def __repr__(self):
        return f'<Project {self.title}>'
