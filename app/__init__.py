"""
File for the app package.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config, TestConfig

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=None):
    """
    This function creates the app and initializes the extensions.
    """
    """Initialize the core application."""
    app = Flask(__name__)

    """Load the configuration from the config file."""
    if config_class is None:
        app.config.from_object(Config)
    elif config_class == 'test':
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(Config)

    """Initialize the extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    """Set up the user loader."""
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    """Import the blueprints."""
    from app.routes.home import home_bp

    """Register the blueprints."""
    app.register_blueprint(home_bp)

    return app
