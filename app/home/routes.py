# The routes from our main view of the application
from flask import render_template
from app.home import bp

# For the current user
from flask_login import login_required, current_user
from app.auth import UserSession
from app.forms import RecipeSearchForm


# Here lalo is going to create a new route
@bp.route("/", methods = ["POST"])
@login_required
def home_post():
    pass

@bp.route("/", methods = ["GET"])
@login_required
def home():
    contex = {
        "user_data" : current_user.query_data(), # The data
        "is_chef" : current_user.is_chef() # Bool
    }
    
    
    # Catch the users data
    return render_template('home.html', **contex)
