from app.extensions import db

class List(db.Model):
    __tablename__ = "list"
    id = db.Column(db.Integer, primary_key = True)
    iduser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    desc = db.Column(db.Text)

    def __init__(self, name : str, iduser : int, desc : str = ""):
        assert isinstance(name, str)
        assert isinstance(desc, str)
        assert isinstance(iduser, int)
        
        self.name = name
        self.desc = desc
        self.iduser = iduser

    def __repr__(self):
        return "<List {} - {}>".format(self.id, self.name)

class ListRecipes(db.Model):
    __tablename__ = "list_recipes"
    id = db.Column(db.Integer, primary_key = True)
    idrecipe = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable = False)
    idlist = db.Column(db.Integer, db.ForeignKey("list.id"), nullable = False)

    def __init__(self, idrecipe : int, idlist : int):
        assert isinstance(idrecipe, int) and isinstance(idlist, int)
        self.idrecipe = idrecipe
        self.idlist = idlist

    def __repr__(self):
        return "<ListRecipes {} - {}".format(self.idlist, self.idrecipe)
