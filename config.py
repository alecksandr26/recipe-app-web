"""
A simple configuration file
"""

import os

# Catch the path from the current file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Fetch some of the veriables from the environment
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
