# The main view of the app
from flask import Blueprint

# Create the main blueprint
bp = Blueprint("home", __name__)


from app.forms import HomeSearchForm


# Create the global contex
@bp.app_context_processor
def home_base():
    return {"search_form" : HomeSearchForm()}




from app.home import routes
