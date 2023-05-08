from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo

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
