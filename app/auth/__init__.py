from flask import Blueprint, render_template, make_response, url_for, abort

from app.models.user import User
from app.models.chef import Chef

from app.extensions import login_manager
from flask_login import UserMixin

bp = Blueprint('auth', __name__, url_prefix = '/auth')

# The code for flask-login

# To define the page where the user will log
login_manager.login_view = 'auth.login'

# To query some user by its id
def query_data_by_id(user_id : int) -> User:
    # Validates that if the user exist by its id otherwise aborts for unauthorized credentials
    assert isinstance(user_id, int)
    return User.query.filter_by(id = user_id).first()

# To create an instance of the user session from a model
class UserSession(UserMixin):
    def __init__(self, user_model : User):
        assert isinstance(user_model, User)
        # It should be always an instance of the user
        self.id = str(user_model.id)

    # To know if the current user is a chef
    def is_chef(self) -> bool:
        chef_model = Chef.query.filter_by(userid = self.id).first()
        return chef_model != None

    # To fetch the data from the user
    def query_data(self):
        return query_data_by_id(int(self.id))

# To catch back from the instance session a use
@login_manager.user_loader
def load_user(user_id : str):
    assert isinstance(user_id, str)  # It should be a pure string instance
    user_model = query_data_by_id(int(user_id))
    
    # If user_model it will throw an unauthorized 401
    return UserSession(user_model) if user_model != None else None 

"""
Check lalo wants our hanlder of what?
Idea put a flash card with the message
"""

# To deal with some unauthorized things
@login_manager.unauthorized_handler
def unauthorized():
    # render a template and pass it as the response body
    return make_response(render_template("auth/unauthorized.html", url_for = url_for), 401)



from app.auth import routes
