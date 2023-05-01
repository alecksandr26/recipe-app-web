from flask import Flask

# Import the configuration
from app.config import Config

# Import all the extensions
from app.extensions import *

# For testing
import unittest

# For the commands
import click

# Import the whole models
from app.models import *

# The function which is going to create the app
def create_app(config_class = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize some Flask extensions here
    db.init_app(app)

    # To initialize bootstrap
    Bootstrap(app)

    # Register the blueprints here
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    from app.recipe import bp as recipe_bp
    app.register_blueprint(recipe_bp)

    # For migrates
    migrate.init_app(app, db)

    # The login manager catches the app instance
    login_manager.init_app(app)

    # Flask commands
    @app.cli.command("test")
    def test():
        # Load the tests
        tests = unittest.TestLoader().discover('test')
        unittest.TextTestRunner().run(tests)

    # To create the the models
    @app.cli.command("models")
    @click.argument("interact")
    def models_interact(interact):
        if interact == "create":
            db.create_all()
        elif interact == "drop":
            db.drop_all()

    return app
