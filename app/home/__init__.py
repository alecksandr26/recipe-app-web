# The main view of the app
from flask import Blueprint

# Create the main blueprint
bp = Blueprint("home", __name__)

from app.home import routes
