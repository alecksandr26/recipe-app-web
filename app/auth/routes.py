# The route from our auth module
from flask import render_template, url_for, request, redirect, flash
from app.auth import bp, UserSession

# documentation: https://flask-login.readthedocs.io/en/latest/
from flask_login import login_user, login_required, logout_user

# Import the forms
from app.forms import LoginForm, SignUpForm

# To hash passwords and check
from werkzeug.security import generate_password_hash, check_password_hash

# DB for users
from app.models.user import User
from app.models.chef import Chef

# To push new data to the database
from app.extensions import db

# To check an email
import re
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


"""
TODO: For each method creats its own function
"""

@bp.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    contex = {
        "url_for" : url_for, # Funcion para generar url a partir de un modelo
        "login_form" : login_form,
        "error" : request.args.get("error") # Saco variables de urls
        # Ejemplo:
        # http://localhost:5000/auth/login?error=That%27s+an+invalid+mail+pal,+learn+how+to+write+one!!!!+%3E%3A(
    }

    if request.method == "POST" and login_form.validate_on_submit():
        # Extact the data from the form :)
        mail = login_form.mail.data
        password = login_form.password.data

        login_form = None
        if re.match(pattern, mail):  # Valid the mail
            # Search the user and return the instance model
            user_model = User.query.filter_by(mail = mail).first()
            print(user_model)
            
            if user_model != None: # Verify that the instance exist
                # Check the password
                # password = from the user text unhash
                # user_model.password = is the hashed password
                if check_password_hash(user_model.password, password):
                    # Create an instance for the session
                    user_session = UserSession(user_model)
                    
                    # Login the user
                    login_user(user_session)
                    return redirect(url_for("home.home")) # redirect the home
                else:
                    return redirect(url_for(
                        "auth.login",
                        error = "Incorrect password dickhead what are you trying to do ? >:|"), code = 303)
            else:
                return redirect(url_for(
                    "auth.login",
                    error = "That mail doesn't exist pal, create an account right now!!! >:("), code = 303)
        else:
            return redirect(url_for(
                "auth.login",
                error = "That's an invalid mail pal, learn how to write one!!!! >:("), code = 303)

    # Unpack the contex
    # **contex = (url_for = url_for, login_form = login_form, error = request..
    return render_template("auth/login.html", **contex)

@bp.route("/signup", methods = ["GET", "POST"])
def signup():
    signup_form = SignUpForm()
    contex = {
        "url_for" : url_for,
        "signup_form" : signup_form,
        "error" : request.args.get("error")
    }
    
    if request.method == "POST" and signup_form.validate_on_submit():
        mail = signup_form.mail.data
        username = signup_form.username.data
        
        if re.match(pattern, mail):  # Valid the mail
            # check if the users exist
            user_model = User.query.filter_by(mail = mail).first()
            if user_model == None:
                # Connect to the database, create a new user and create a new session
                password = signup_form.password.data
                is_chef = signup_form.is_chef.data # Booleano
                signup_form = None
                
                # Create a new instance of the model user
                user_model = User(username = username,
                                  password = generate_password_hash(password), mail = mail)

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

                # flashing Is not working 
                flash("Account created baby >:)")
                
                return redirect(url_for("home.home"))
            else:
                # url_for("auth.signup", error = "esto es un error")
                # /auth/signup?error=esto%27s+es+un+error
                # nos redirigimos a /auth/signup?error=esto%27s+es+un+error
                return redirect(url_for(
                    "auth.signup",
                    error = "That mail already exists pal, use another!!! >:("), code = 303)
        else:
            return redirect(url_for(
                "auth.signup",
                error = "That's an invalid mail pal, learn how to write one!!!! >:("), code = 303)
    
    
    return render_template("auth/signup.html", **contex)


@bp.route("/logout", methods = ["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"), code = 303)
