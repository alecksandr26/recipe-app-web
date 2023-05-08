"""
A simple configuration file
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Fetch some of the veriables from the environment
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Creates a database on the project dir
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,
                                                                                     'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    WTF_CSRF_ENABLED = True
