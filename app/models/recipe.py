from app.extensions import db

# The recipe model
class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key = True)
    ingredients = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    portions = db.Column(db.Integer)
    idcategory = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = False)
    url = db.Column(db.Text)
    name = db.Column(db.Text, nullable = False)
    preptime = db.Column(db.String(25))
    cooktime = db.Column(db.String(25))

    def __init__(self, ingredients : str, idcategory : int, instructions : str, name : str,
                 portions : int = None, url : str = None, preptime : str = None, cooktime : str = None):
        # Assert each argument
        assert isinstance(ingredients, str) \
            and isinstance(idcategory, int) \
            and isinstance(instructions, str) \
            and isinstance(name, str)

        if portions != None:
            assert isinstance(portions, int)
        if url != None:
            assert isinstance(url, str)
        if preptime != None:
            assert isinstance(preptime, int)
        if cooktime != None:
            assert isinstance(cooktime, int)

        self.name = name
        self.ingredients = ingredients
        self.idcategory = idcategory
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

    def __init__(self, name : str, unit : str, idrecipe : int, amount : int = None):
        assert isinstance(name, str) and isinstance(unit, str) \
            and isinstance(idrecipe, int)

        if amount != None:
            assert isinstance(amount, int)

        self.name = name
        self.unit = unit
        self.idrecipe = idrecipe
        self.amount = amount

    def __repr__(self):
        return "<NutritionalEle {} - {}>".format(self.idrecipe, self.name)
    
