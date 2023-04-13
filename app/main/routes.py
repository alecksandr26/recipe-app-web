# The routes from our main view of the application
from flask import render_template
from app.main import bp
from app.extensions import db
from sqlalchemy import text


@bp.route("/home")
def index():
    con = db.engine.connect()
    result = con.execute(text("CREATE TABLE hello(id integer);"))
    con.commit()
    return render_template('index.html')
