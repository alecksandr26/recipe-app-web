from flask import Flask

# Import the configuration
from config import Config

# The function which is going to create the app
def create_app(config_class = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize some Flask extensions here

    # Register the blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    

    @app.route("/tests/")
    def test_page():
        return "Hello boooooyyy"
    
    return app
