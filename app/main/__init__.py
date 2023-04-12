# The main view of the app

from flask import Blueprint

# Create the main blueprint
bp = Blueprint('main', __name__)

from app.main import routes
