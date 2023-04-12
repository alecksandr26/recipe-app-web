from app.extensions import db

# The user model 
class User(db.Model):
    __tablename__ = "users"
    # By default it is set to not null
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    mail = db.Column(db.String(50))
    password = db.Column(db.String(50), nullable = False)
