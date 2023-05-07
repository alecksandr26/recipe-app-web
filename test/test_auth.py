from flask_testing import TestCase
from flask import current_app, url_for
from app import create_app

# For connectity TO the database
from app.extensions import db
from sqlalchemy import text


class AuthTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI  # Load the db connection
        app.config['TESTING'] = True  # Set the app in testing mode
        return app


    def test_login(self):
        pass
