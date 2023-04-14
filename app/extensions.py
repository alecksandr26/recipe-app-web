"""
The extensions and its configurations of some of them
"""

# To connect to the postgres db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# To have bootstrap
# https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_bootstrap import Bootstrap

# Flask login manager
from flask_login import LoginManager

# For the database
db = SQLAlchemy()

# For migrates
migrate = Migrate()

# For the login sessions of the users
login_manager = LoginManager()

# Import the whole configurations from the auth with flask-login
from app.auth import *

