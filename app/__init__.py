from flask import Flask


# Import the configuration
from config import Config

# Import the extensions
from app.extensions import db

# The function which is going to create the app
def create_app(config_class = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize some Flask extensions here
    db.init_app(app)

    # Register the blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    @app.route("/tests/")
    def test_page():
        return "Hello boooooyyy"
    
    return app
