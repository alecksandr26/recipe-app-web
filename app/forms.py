"""
The whole forms from the app

https://wtforms.readthedocs.io/en/3.0.x/
"""

# Import the flask form
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

# To know if the user is a chef or not 
# from flask_login import current_user

# Automize the forms
class LoginForm(FlaskForm):
    mail = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Submit")

# Automize the signup forms
class SignUpForm(FlaskForm):
    username = StringField("UserName", validators = [DataRequired()])
    mail = StringField("Email", validators = [DataRequired()])
    password = PasswordField("New Password", [
        DataRequired(),
        EqualTo("confirm", message = "Passwords must match")
    ])
    confirm = PasswordField("Repeat Password", [DataRequired()])
    accept_tos = BooleanField("I accept the TOS", [DataRequired()])
    is_chef = BooleanField("Are you a chef?")
    submit = SubmitField("Submit")


class SettingsForm(FlaskForm):
    username = StringField("New UserName")
    mail = StringField("New Email")
    password = PasswordField("New Password", validators = [
        EqualTo("confirm", message = "Passwords must match")
    ])
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Submit")

class RecipeCreateForm(FlaskForm):
    name = StringField("Name")
    desc = TextAreaField("Description")
    instru = TextAreaField("Instructions")
    submit = SubmitField("Submit")
    

class RecipeSearchForm(FlaskForm):
    name = StringField("Search name")
    submit = SubmitField("Submit")
