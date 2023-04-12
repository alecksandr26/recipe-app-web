from app.extensions import db

# The recipe model
class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    portions = db.Column(db.Integer)
    idcategory = db.Column(db.Integer, ForeignKey("category.id"))
    url = db.Column(db.Text)
    
    
    
