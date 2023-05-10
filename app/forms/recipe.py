"""
The whole forms from the app

https://wtforms.readthedocs.io/en/3.0.x/
"""

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, TextAreaField, \
    IntegerField, URLField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from app.models import Category

class RecipeCreateForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    category = SelectField("Category", validators=[DataRequired()], choices=[], coerce=int)
    desc = TextAreaField("Description", validators = [DataRequired()])
    ingre = TextAreaField("Ingredients", validators=[DataRequired()])
    instru = TextAreaField("Instructions", validators = [DataRequired()])
    portions = IntegerField("Portions", validators=[NumberRange(min=1, max=20)], default = 1)
    url = URLField("Image url")
    preptime = StringField("Preparation time")
    cooktime = StringField("Cook time")
    add_to_favorites = BooleanField("Add to Favorites?")
    submit = SubmitField("Create")


    # Construct the forms and get the choices from the database
    def __init__(self, *args, **kwargs):
        super(RecipeCreateForm, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id, c.name) for c in Category.query.all()]
        
# The people can comment recipes
class RecipeCommentForm(FlaskForm):
    pass


# Create the recipe form
class RecipeUpdateForm(FlaskForm):
    new_name = StringField("New Name")
    new_category = SelectField("New Category", choices=[], coerce=int)
    new_desc = TextAreaField("New Description")
    new_ingre = TextAreaField("New Ingredients")
    new_instru = TextAreaField("New Instructions")
    new_portions = IntegerField("New Portions", validators=[NumberRange(min=1, max=20)], default = 1)
    new_url = URLField("New Image url")
    new_preptime = StringField("New Preparation time")
    new_cooktime = StringField("New Cook time")
    # We are going to create our own submit button
    # submit = SubmitField("Save")

    # Construct the forms and get the choices from the database
    def __init__(self, *args, **kwargs):
        super(RecipeUpdateForm, self).__init__(*args, **kwargs)
        self.new_category.choices = [(c.id, c.name) for c in Category.query.all()]
