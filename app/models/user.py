from app.extensions import db

# The user model 
class User(db.Model):
    __tablename__ = "user"
    # By default it is set to not null
    id = db.Column(db.Integer, primary_key = True)
    mail = db.Column(db.String(50), nullable = False, unique = True)    
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(), nullable = False)    

    def __init__(self, username : str, password : str, mail : str):
        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(mail, str)
        
        self.username = username
        self.password = password
        self.mail = mail

    def __repr__(self):
        return "<User {} - {}>".format(self.id, self.username)

    
