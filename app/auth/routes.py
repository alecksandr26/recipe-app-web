# The route from our auth module
from flask import render_template, url_for, request, redirect, flash
from app.auth import bp, UserSession

# documentation: https://flask-login.readthedocs.io/en/latest/
from flask_login import login_user, login_required, logout_user, current_user

# Import the forms
from app.forms import LoginForm, SignUpForm, SettingsForm

# To hash passwords and check
from werkzeug.security import generate_password_hash, check_password_hash

# DB for users
from app.models import User
from app.models import Chef

# To push new data to the database
from app.extensions import db


import pdb

# To check an email
import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

@bp.route('/login', methods = ["POST"])
def login_post():
    login_form = LoginForm()
    if not login_form.validate_on_submit():  #  Validate the form
        return redirect(url_for("auth.login"), code = 303)

    mail = login_form.mail.data
    password = login_form.password.data
    login_form = None
    if not re.match(pattern, mail):  # Valid the mail
        return redirect(url_for(
            "auth.login",
            error = "That's an invalid mail pal, learn how to write one!!!! >:("), code = 303)
    
    # Search the user and return the instance model
    user_model = User.query.filter_by(mail = mail).first()
    
    if not user_model != None: # Verify that the instance exist
        return redirect(url_for(
            "auth.login",
            error = "That mail doesn't exist pal, create an account right now!!! >:("), code = 303)

    # Check the password
    # password = from the user text unhash
    # user_model.password = is the hashed password
    if not check_password_hash(user_model.password, password):
        return redirect(url_for(
            "auth.login",
            error = "Incorrect password bughead what are you trying to do ? >:|"), code = 303)

    # Create an instance for the session
    user_session = UserSession(user_model)
                    
    # Login the user
    login_user(user_session)
    return redirect(url_for("home.home"), code = 302) # redirect the home with OK status
    
@bp.route("/login", methods = ["GET"])
def login():
    login_form = LoginForm()
    contex = {
        "url_for" : url_for, # Funcion para generar url a partir de un modelo
        "login_form" : login_form,
        "error" : request.args.get("error") # Saco variables de urls
        # Ejemplo:
    # http://localhost:5000/auth/login?error=That%27s+an+invalid+mail+pal,+learn+how+to+write+one!!!!+%3E%3A(
    }

    # Unpack the contex
    # **contex = (url_for = url_for, login_form = login_form, error = request..
    return render_template("auth/login.html", **contex)


@bp.route("/signup", methods = ["POST"])
def signup_post():
    signup_form = SignUpForm()
    mail = signup_form.mail.data
    
    if not (signup_form.validate_on_submit() and re.match(pattern, mail)):
        return redirect(url_for(
            "auth.signup",
            error = "That's an invalid mail pal, learn how to write one!!!! >:("), code = 303)
    

    username = signup_form.username.data
    
    # check if the users exist
    user_model = User.query.filter_by(mail = mail).first()        

    if  user_model != None:
        # url_for("auth.signup", error = "esto es un error")
        # /auth/signup?error=esto%27s+es+un+error
        # nos redirigimos a /auth/signup?error=esto%27s+es+un+error
        return redirect(url_for(
            "auth.signup",
            error = "That mail already exists pal, use another!!! >:("), code = 303)
    

    # Connect to the database, create a new user and create a new session
    password = signup_form.password.data
    is_chef = signup_form.is_chef.data # Booleano
    signup_form = None


    
    # Create a new instance of the model user
    user_model = User(username = username,
                      password = generate_password_hash(password),
                      mail = mail)
        
    # Push the data
    db.session.add(user_model)
    db.session.commit()

    # Push if it is chef
    if is_chef:    # Append to the cheff table
        user_id = User.query.filter_by(mail = user_model.mail).first().id
        chef_model = Chef(int(user_id))
        
        # Push data
        db.session.add(chef_model)
        db.session.commit()
                
    # Create the session and login it
    user_session = UserSession(user_model)
    login_user(user_session)
    
    return redirect(url_for("home.home"), code = 302)
        


@bp.route("/signup", methods = ["GET"])
def signup():
    signup_form = SignUpForm()
    
    contex = {
        "url_for" : url_for,
        "signup_form" : signup_form,
        "error" : request.args.get("error")
    }
    
    return render_template("auth/signup.html", **contex)


@bp.route("/logout", methods = ["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"), code = 303)


@bp.route("/settings", methods = ["POST"])
@login_required
def settings_post():
    settings_form = SettingsForm()
    if not settings_form.validate_on_submit():
        return redirect(url_for("auth.settings"), code = 303)

    user_model = User.query.filter_by(id = current_user.id).first()
    mail = settings_form.mail.data

    if mail != "":
        if not re.match(pattern, mail):
            return redirect(url_for(
                "auth.settings",
                error = "Hey bug head, learn how to write an email"), code = 303)
        user_model.mail = mail
    
    username = settings_form.username.data
    if username != "":
        user_model.username = username

    password = settings_form.password.data
    if password != "":
        user_model.password = password

    db.session.commit()
    return redirect(url_for("home.home"), code = 302)  # Redirect to the home OK
    

@bp.route("/settings", methods = ["GET"])
@login_required
def settings():
    settings_form = SettingsForm()
    contex = {
        "url_for" : url_for,
        "settings_form" : settings_form,
        "error" : request.args.get("error")
    }
    
    return render_template("auth/settings.html", **contex)

