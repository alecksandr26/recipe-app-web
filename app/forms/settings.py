from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo

class SettingsForm(FlaskForm):
    username = StringField("New UserName")
    mail = StringField("New Email")
    password = PasswordField("New Password", validators = [
        EqualTo("confirm", message = "Passwords must match")
    ])
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Submit")
