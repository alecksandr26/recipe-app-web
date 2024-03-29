from flask import Flask, request
import requests
from flask_wtf.csrf import CSRFProtect

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
from werkzeug.wrappers import Request, Response

# again middleware
class HTTPMethodOverrideMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if "_method" in request.form:
            method = request.form["_method"].upper()
            if method in ["PUT"]:
                environ["REQUEST_METHOD"] = method

        return self.app(environ, start_response)
            

# The function which is going to create the app
def create_app(config_class = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable csrf protection
    csrf = CSRFProtect(app)
    
    # Initialize some Flask extensions here
    db.init_app(app)            # Initialize the db 

    Bootstrap(app)              # Allow the bootstrap 

    # Configure the cors 
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

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
    @click.option('--file', default = None, help = 'Path to a specific test file')
    def test(file):
        if file:
            tests = unittest.TestLoader().discover('test', pattern = file.split('/')[-1])
        else:
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


    # Add the middleware
    # app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app
