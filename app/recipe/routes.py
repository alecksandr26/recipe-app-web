# The route from our auth module
from flask import render_template, url_for, request, redirect, flash
from app.recipe import bp

# documentation: https://flask-login.readthedocs.io/en/latest/
from flask_login import login_user, login_required, logout_user, current_user

# To push new data to the database
from app.extensions import db
from app.forms import RecipeCreateForm, RecipeSearchForm

@bp.route('/search', methods = ["GET", "POST"])
@login_required
def search():
    recipe_search_form = RecipeSearchForm()
    
    contex = {
        "url_for" : url_for,
        "recipe_search_form" : recipe_search_form
    }

    return render_template("recipe/search.html", **contex)

@bp.route("/create", methods = ["GET", "POST"])
@login_required
def create():
    recipe_create_form = RecipeCreateForm()
    
    contex = {
        "url_for" : url_for,
        "recipe_create_form" : recipe_create_form
    }
    
    return render_template("recipe/create.html", **contex)
