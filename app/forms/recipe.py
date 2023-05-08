"""
The whole forms from the app

https://wtforms.readthedocs.io/en/3.0.x/
"""

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RecipeCreateForm(FlaskForm):
    name = StringField("Name")
    desc = TextAreaField("Description")
    instru = TextAreaField("Instructions")
    submit = SubmitField("Submit")
    

class RecipeSearchForm(FlaskForm):
    name = StringField("Search name")
    submit = SubmitField("Submit")
