# The routes from our main view of the application
from flask import render_template, request, redirect
from app.home import bp

# For the current user
from flask_login import login_required, current_user
from app.auth import UserSession
from app.forms import HomeSearchForm
from app.models import Recipe, List, ListRecipes




# A global home_contex
home_contex = {}

# Here lalo is going to create a new route
@bp.route("/", methods = ["POST"])
@login_required
def home_post():
    search_form = HomeSearchForm()
    if not search_form.validate_on_submit() or home_contex == {}:
        return redirect(url_for('home.home', error = "What are you trying to do? >:|"), code = 303)

    data = search_form.query.data

    # Search that pattern
    print(data)
    return render_template('home.html', **home_contex)


@bp.route("/", methods = ["GET"])
@login_required
def home():
    global home_contex               # Bring the global home_contex
    home_contex = {
        "user_data" : current_user.query_data(),
        "is_chef" : current_user.is_chef(),
        "error" : request.args.get("error"),
        "data" : set()
    }

    # Bring the recipes from the user
    id_favorites_list = current_user.query_favorites_list().id
    list_recipes = ListRecipes.query.filter_by(idlist = id_favorites_list).all()

    # Append the lists
    for lr in list_recipes:
        home_contex["data"].add(Recipe.query.filter_by(id = lr.idrecipe).first())

    # Catch the users data
    return render_template('home.html', **home_contex)
