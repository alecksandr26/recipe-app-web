from app.extensions import db

# The chef Model
class Chef(db.Model):
    __tablename__ = "chef"
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    
    def __init__(self, userid : int):
        assert isinstance(userid, int)
        self.userid = userid

    def __repr__(self):
        return "<Chef {} - {}".format(self.id, self.userid)



