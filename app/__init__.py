from flask import Flask, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # bind db with app
    db.init_app(app)

    # Force clear session on restart
    app.config["FIRST_REQUEST_AFTER_RESTART"] = True

    @app.before_request
    def clear_session_on_restart():
        if app.config["FIRST_REQUEST_AFTER_RESTART"]:
            session.clear()
            app.config["FIRST_REQUEST_AFTER_RESTART"] = False
            if not request.endpoint or "auth.login" not in request.endpoint:
                return redirect(url_for("auth.login"))

    # Blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(task_bp, url_prefix="/")

    return app
