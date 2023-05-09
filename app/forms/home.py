from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class HomeSearchForm(FlaskForm):
    query = StringField("", validators = [DataRequired()], render_kw={"placeholder": "Recipe..."})
    submit = SubmitField("Search")

    
