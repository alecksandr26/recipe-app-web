# The routes from our main view of the application
from flask import render_template, request, redirect, url_for
from app.home import bp

# For the current user
from flask_login import login_required, current_user
from app.auth import UserSession
from app.forms import HomeSearchForm
from app.models import Recipe, List, ListRecipes
from sqlalchemy import or_

# A global home_contex
home_contex = {
    "searched" : False
}

# Here lalo is going to create a new route
@bp.route("/", methods = ["POST"])
@login_required
def home_post():
    search_form = HomeSearchForm()
    if not search_form.validate_on_submit():
        return redirect(url_for('home.home', error = "What are you trying to do? >:|"), code = 303)

    data = search_form.query.data
    recipes = Recipe.query.filter(or_(Recipe.name.ilike(f"%{data}%"),
                                  Recipe.description.ilike(f"%{data}%"),
                                  Recipe.ingredients.ilike(f"%{data}%"))).all()

    home_contex["searched"] = True
    home_contex["data_searched"] = set(recipes)

    # Search that pattern
    return render_template('home.html', **home_contex)


@bp.route("/", methods = ["GET"])
@login_required
def home():
    global home_contex               # Bring the global home_contex
    
    home_contex["searched"] = False
    home_contex["user_data"] = current_user.query_data()
    home_contex["is_chef"] = current_user.is_chef()
    home_contex["error"] = request.args.get("error")
    home_contex["data"] = set()

    # Bring the recipes from the user
    id_favorites_list = current_user.query_favorites_list().id
    list_recipes = ListRecipes.query.filter_by(idlist = id_favorites_list).all()

    # Append the favorites elements
    for lr in list_recipes:
        home_contex["data"].add(Recipe.query.filter_by(id = lr.idrecipe).first())

    # Catch the users data
    return render_template('home.html', **home_contex)
