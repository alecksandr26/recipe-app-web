# The route from our auth module
from flask import render_template, url_for, request, redirect, jsonify
from app.recipe import bp

# documentation: https://flask-login.readthedocs.io/en/latest/
from flask_login import login_user, login_required, logout_user, current_user

# To push new data to the database
from app.extensions import db
from app.forms import RecipeCreateForm, HomeSearchForm, RecipeCreateForm, RecipeUpdateForm
from app.models import Recipe, List, ListRecipes, User, Category

# To allow the corss origins
from flask_cors import cross_origin


import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # scheme
    r'(?:[\w-]+\.)+[\w-]+(?:\:[\d]+)?'  # domain and optional port
    r'(?:(?:/[\w#!:.?+=&%@!\-\/]*)|\b|$)'  # path and query parameters
    , re.IGNORECASE)

@bp.route("/create", methods = ["POST"])
@login_required
def create_post():
    recipe_create_form = RecipeCreateForm()
    if not recipe_create_form.validate_on_submit():
        return redirect(url_for("recipe.create", error = "You written something wrong pal :|"), code = 303)

    # Check the url
    url_string = recipe_create_form.url.data
    if url_string != "" and not url_regex.match(url_string):
        return redirect(url_for("recipe.create", error = "Learn how you to write an god damn URL >:|"),
                        code = 303)
    
    # Create a new recipe
    recipe_model = Recipe(recipe_create_form.ingre.data,
                          recipe_create_form.category.data,
                          recipe_create_form.instru.data,
                          recipe_create_form.name.data,
                          recipe_create_form.desc.data,
                          int(current_user.id),
                          recipe_create_form.portions.data,
                          recipe_create_form.url.data,
                          recipe_create_form.preptime.data,
                          recipe_create_form.cooktime.data)
    
    db.session.add(recipe_model)
    
    # If the user wants to add this recipe to the its favories
    if recipe_create_form.add_to_favorites.data:
        id_favorites_list = current_user.query_favorites_list().id  # Get from the favories list recipe fetchsid
        list_recipes = ListRecipes(recipe_model.id, id_favorites_list)
        db.session.add(list_recipes)

    db.session.commit()
    return redirect(url_for("home.home"), code = 302)


@bp.route("/create", methods = ["GET"])
@login_required
def create():
    contex = {
        "url_for" : url_for,
        "recipe_create_form" : RecipeCreateForm(),
        "error" : request.args.get("error")
    }
    
    return render_template("recipe/create.html", **contex)


# To watch detiled the card
@bp.route("/<int:id>", methods = ["GET"])
@login_required
def view(id : int):

    contex = {"error" : request.args.get("error")}
    # Made the query
    recipe_model = Recipe.query.filter_by(id = id).first()

    if recipe_model == None:
        return redirect(url_for("home.home", error = "Hey that recipe doesn't exist pal :|"), code = 303)

    contex["recipe"] = recipe_model

    # Fetch the owner name of the recipe
    owner = User.query.filter_by(id = recipe_model.iduser).first()
    if owner.id == int(current_user.id):
        contex["owner"] = "you"
        contex["is_owner"] = True
    else:
        contex["owner"] = owner.username
        contex["is_owner"] = False


    # Finally fetch the category name
    contex["category_name"] = Category.query.filter_by(id = recipe_model.idcategory).first().name
    
    return render_template("recipe/view.html", **contex)

@bp.route("/<int:id>/edit", methods = ["PUT"])
@login_required
def update(id : int):
    recipe_update_form = RecipeUpdateForm()

    recipe = Recipe.query.filter_by(id = id).first()

    if recipe == None:
        return jsonify({"message" : f"The recipe {id} doesn't exist what are you doing pal >:|",
                        "success" : False})
    
    if recipe.iduser != int(current_user.id):
        return jsonify({"message" : f"The recipe {id} doesn't belong to you pal >:|",
                        "success" : False})

    print(recipe_update_form.data)
    if recipe_update_form.new_category.data:
        recipe.idcategory = recipe_update_form.new_category.data

    if recipe_update_form.new_name.data:
        recipe.name = recipe_update_form.new_name.data


    # Update the recipe
    db.session.commit()
    return jsonify({"message" : f"Recipe {recipe.id} updated", "success" : True})

@bp.route("/<int:id>/edit", methods = ["GET"])
@login_required
def edit(id : int):

    recipe = Recipe.query.filter_by(id = id).first()
    if recipe == None:
        return redirect(url_for("home.home",
                                error = f"The recipe {id} doesn't exist what are you doing pal >:|"),
                        code = 303)
    
    contex = {"error" : request.args.get("get")}
    contex["recipe_update_form"] = RecipeUpdateForm()
    contex["recipe"] = recipe

    # Finally fetch the category name
    contex["category_name"] = Category.query.filter_by(id = recipe.idcategory).first().name
    return render_template("recipe/edit.html", **contex)

    
@bp.route("/<int:id>", methods = ["DELETE"])
@login_required
def delete(id : int):
    # For the moment redirects back to the home
    recipe_model = Recipe.query.filter_by(id = id).first()


    if recipe_model == None:
        return jsonify({"message" : f"The recipe {id} doesn't exist what are you doing pal >:|",
                        "success" : False})

    if recipe_model.iduser != int(current_user.id):
        return jsonify({"message" : f"The recipe {id} doesn't belong to you pal >:|",
                        "success" : False})

    # Delete the recipe from all the lists
    list_recipes = ListRecipes.query.filter_by(idrecipe = recipe_model.id).delete()
    # Deletes the recipe
    db.session.delete(recipe_model)
    db.session.commit()
    
    return jsonify({"message" : f"Recipe {id} deleted", "success" : True})




