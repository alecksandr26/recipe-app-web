# The route from our auth module
from flask import render_template, url_for, request, redirect, flash
from app.recipe import bp

# documentation: https://flask-login.readthedocs.io/en/latest/
from flask_login import login_user, login_required, logout_user, current_user

# To push new data to the database
from app.extensions import db
from app.forms import RecipeCreateForm, RecipeSearchForm, HomeSearchForm


@bp.route("/create", methods = ["POST"])
@login_required
def create_post():
    recipe_create_form = RecipeCreateForm()
    return redirect(url_for("home.home"), code = 302)


@bp.route("/create", methods = ["GET"])
@login_required
def create():
    contex = {
        "url_for" : url_for,
        "recipe_create_form" : RecipeCreateForm(),
        "search_form" : HomeSearchForm(),
        "error" : request.args.get("error")
    }
    
    return render_template("recipe/create.html", **contex)
