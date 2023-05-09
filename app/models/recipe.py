from app.extensions import db
from datetime import datetime

# The recipe model
class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    portions = db.Column(db.Integer)
    idcategory = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = False)
    url = db.Column(db.Text)
    name = db.Column(db.Text, nullable = False)
    preptime = db.Column(db.String(25))
    cooktime = db.Column(db.String(25))
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    iduser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    def __init__(self, ingredients : str, idcategory : int, instructions : str, name : str, description : str,
                 iduser: int, portions : int = 1, url : str = "", preptime : str = "", cooktime : str = ""):
        # Assert each argument

        print("protions: ", portions)
        assert isinstance(ingredients, str) 
        assert isinstance(idcategory, int) 
        assert isinstance(instructions, str) 
        assert isinstance(name, str) 
        assert isinstance(url, str) 
        assert isinstance(preptime, str) 
        assert isinstance(cooktime, str)
        assert isinstance(portions, int)

        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.idcategory = idcategory
        self.iduser = iduser
        self.instructions = instructions
        self.portions = portions
        self.url = url
        self.preptime = preptime
        self.cooktime = cooktime


    def __repr__(self):
        return "<Recipe {} - {}>".format(self.id, self.name)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    idrecipe = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    comment = db.Column(db.Text, nullable = False)

    def __init__(self, idrecipe : int, comment : str):
        assert isinstance(idrecipe, int) and isinstance(comment, str)

        self.idrecipe = idrecipe
        self.comment = comment

    def __repr__(self):
        return "<Comment {} - {}".format(self.idrecipe, self.comment)

class NutritionalEle(db.Model):
    __tablename__ = "nutritional_ele"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    unit = db.Column(db.String(50), nullable = False)
    idrecipe = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    amount = db.Column(db.Float)

    def __init__(self, name : str, unit : str, idrecipe : int, amount : float = 0.0):
        assert isinstance(name, str) and isinstance(unit, str) \
            and isinstance(idrecipe, int) \
            and isinstance(amount, float)

        self.name = name
        self.unit = unit
        self.idrecipe = idrecipe
        self.amount = amount

    def __repr__(self):
        return "<NutritionalEle {} - {}>".format(self.idrecipe, self.name)
    
