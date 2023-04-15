from app.extensions import db

# This is the category model
class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)

