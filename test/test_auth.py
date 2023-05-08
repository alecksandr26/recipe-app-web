from flask_testing import TestCase
from flask import current_app, url_for, session
from flask_login import current_user
from flask_wtf.csrf import generate_csrf


# For connectity TO the database
from app.extensions import db
from sqlalchemy import text

# Import the configuration
from app.config import Config

# Import the needed models for testing
from app.models import User, Chef

# Bring the needed forms
from app.forms import *

# fetch the create app function
from app import create_app

# Fetch the base dir
import os
basedir = os.path.abspath(os.path.dirname(__file__))

import pdb

class LoginTestCase(TestCase):
    def create_app(self):
        # Re configurate
        Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        Config.TESTING = True
        Config.WTF_CSRF_ENABLED = False
        return create_app()  # Create the app with the configuration

    # Simulates that a user exist
    def setUp(self):
        self.test_user = {
            "username" : "pedrito",
            "password" : "pedrito",
            "mail" : "pedrito@gmail.com"
        }
        
        db.create_all()
        new_user = User(**self.test_user)  # Unpack the test user
        db.session.add(new_user)
        db.session.commit()

    # Remove all the users
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    
    def test_login_post(self):
        login_form = LoginForm(data = self.test_user)
        
        # send a POST request to the login route with the login form data
        response = self.client.post(url_for('auth.login_post'), data = login_form.data,
                                    follow_redirects = True)
        
        # Checks that we have been redirected with the status 200
        self.assertEqual(response.status_code, 200)

        
    def test_login_get(self):   # Test the simple page
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)


        
class SignupTestcase(TestCase):
    def create_app(self):
        # Re configurate
        Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        Config.TESTING = True
        Config.WTF_CSRF_ENABLED = False
        return create_app()  # Create the app with the configuration

    # Simulates that a user exist
    def setUp(self):
        self.test_user = {
            "username" : "pedrito",
            "password" : "pedrito",
            "confirm" : "pedrito",
            "mail" : "pedrito@gmail.com",
            "accept_tos" : True,
            "is_chef" : True
        }
        db.create_all()

    # Remove all the users
    def tearDown(self):
        # pdb.set_trace()
        db.drop_all()

    def test_signup_get(self):   # Test the simple page
        response = self.client.get(url_for("auth.signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_post(self): # Test the creation of users
        signup_form = SignUpForm(data = self.test_user)

        # send a POST request to the login route with the login form data
        response = self.client.post(url_for("auth.signup_post"), data = signup_form.data,
                                    follow_redirects = True)

        self.assertEqual(response.status_code, 200)  # Returned to home
        user_model = User.query.filter_by(mail = self.test_user["mail"]).first()
        self.assertIsNotNone(user_model)


class SettingsTestCase(TestCase):
    def create_app(self):
        # Re configurate
        Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        Config.TESTING = True
        Config.WTF_CSRF_ENABLED = False
        return create_app()  # Create the app with the configuration

    def setUp(self):
        self.test_user = {
            "username" : "pedrito",
            "password" : "pedrito",
            "confirm" : "pedrito",
            "mail" : "pedrito@gmail.com",
            "accept_tos" : True,
            "is_chef" : True
        }
        db.create_all()

    def tearDown(self):
        db.drop_all()
    
    def test_settings_get(self):
        self.post_new_user()    # Creat new user to be able to be required
        response = self.client.get(url_for("auth.settings"))
        self.assertEqual(response.status_code, 200)

    def post_new_user(self):    # A simple method to post some user
        signup_form = SignUpForm(data = self.test_user)

        # send a POST request to the login route with the login form data
        response = self.client.post(url_for("auth.signup_post"), data = signup_form.data,
                                    follow_redirects = True)

        self.assertEqual(response.status_code, 200)  # Returned to home
        

    def test_settings_post(self):
        self.post_new_user()
        data = {"username" : "pedrito2",
                "mail" : "",
                "password" : ""}
        settings_form = SettingsForm(data = data)

        # send a POST request to the login route with the login form data
        response = self.client.post(url_for("auth.settings_post"), data = settings_form.data,
                                    follow_redirects = True)

        self.assertEqual(response.status_code, 200)  # Ok

        


        
