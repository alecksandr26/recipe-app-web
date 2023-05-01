from flask import Blueprint, render_template, make_response, url_for, abort


bp = Blueprint('recipe', __name__, url_prefix = '/recipe')

from app.recipe import routes
