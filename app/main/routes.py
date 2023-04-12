# The routes from our main view of the application
from flask import render_template
from app.main import bp

@bp.route("/home")
def index():
    return render_template('index.html')
