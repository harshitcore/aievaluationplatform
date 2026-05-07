from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-123'
    
    import sys
    
    # Check if Render has provided a Cloud Database URL
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # Fix Render's URL format for SQLAlchemy
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # If no cloud DB is found, fallback to local SQLite
        if getattr(sys, 'frozen', False):
            basedir = os.path.dirname(sys.executable)
        else:
            basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    migrate.init_app(app, db)

    from app.models import user, project, evaluation, response

    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.projects import projects_bp
    from app.routes.evaluation import eval_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(eval_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return user.User.query.get(int(user_id))

    return app
