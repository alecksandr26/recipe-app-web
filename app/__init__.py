from flask import Flask

# Import the configuration
from app.config import Config

# Import the extensions like database and migrates
from app.extensions import db, migrate

# The function which is going to create the app
def create_app(config_class = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize some Flask extensions here
    db.init_app(app)

    # Register the blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # For migrates
    migrate.init_app(app, db)
    
    return app
