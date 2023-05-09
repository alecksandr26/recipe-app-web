"""
The extensions and its configurations of some of them
"""

# To connect to the postgres db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask login manager
from flask_login import LoginManager

# To have bootstrap
# https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_bootstrap import Bootstrap

# Import the flask-cors
from flask_cors import CORS

# For the database
db = SQLAlchemy()

# Initialize the migrations instnace
migrate = Migrate()

# Initialize the manager for users login
login_manager = LoginManager()

# Import the whole configurations from the auth with flask-login
from app.auth import *
