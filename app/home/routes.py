# The routes from our main view of the application
from flask import render_template, request, redirect
from app.home import bp

# For the current user
from flask_login import login_required, current_user
from app.auth import UserSession
from app.forms import HomeSearchForm
from app.models import Recipe


# A global contex
contex = {}


# Here lalo is going to create a new route
@bp.route("/", methods = ["POST"])
@login_required
def home_post():
    search_form = HomeSearchForm()
    if not search_form.validate_on_submit() or contex == {}:
        return redirect(url_for('home.home', error = "What are you trying to do?"), code = 303)

    data = search_form.query.data
    print(data)
    
    return render_template('home.html', **contex)

@bp.route("/", methods = ["GET"])
@login_required
def home():
    global contex               # Bring the global contex
    contex = {
        "user_data" : current_user.query_data(),
        "is_chef" : current_user.is_chef(),
        "error" : request.args.get("error"),
        "data" : list(),
        "search_form" : HomeSearchForm()
    }

    # Bring the recipes from the user

    
    # Catch the users data
    return render_template('home.html', **contex)
