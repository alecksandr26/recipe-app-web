from flask_testing import TestCase
from flask import current_app, url_for
from app import create_app

# For connectity TO the database
from app.extensions import db
from sqlalchemy import text

# Import the configuration
from app.config import Config

class DBTestCases(TestCase):
    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI  # Load the db connection
        app.config['TESTING'] = True  # Set the app in testing mode
        return app
    
    # Check if the app exist
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # Check connectity to the database
    def test_connect_db(self):
        engine = db.engine
        with engine.connect() as conn:
            # Send a simple message and receive it back
            result = conn.execute(text("SELECT 1"))
            self.assertEqual(result.fetchone()[0], 1)
