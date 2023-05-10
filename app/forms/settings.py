from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo

class SettingsForm(FlaskForm):
    username = StringField("New UserName")
    mail = StringField("New Email")
    currentpassword = PasswordField("Current Password")
    password = PasswordField("New Password", validators = [
        EqualTo("confirm", message = "Passwords must match")
    ])
    confirm = PasswordField("Repeat New Password")
    submit = SubmitField("Save")
