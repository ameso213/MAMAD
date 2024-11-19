from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.extensions import db, migrate  # Assuming these are defined in app/extensions.py
import os

# Config class to handle configuration settings
class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/mamad_api'

    # JWT secret key configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'MAMAD256')


# Initialize extensions
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    # Example blueprint for authentication (you can uncomment and modify as needed)
    # from app.controllers.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    # Define the root route
    @app.route('/')
    def home():
        return "hello"

    return app
