from app import db

class User(db.Model):
    f_name = db.Column(db.String(70), unique=False)
    l_name= db.Column(db.String(70), unique=False)
    email = db.Column(db.String(100), unique=False)
    feedback = db.Column(db.String(200), unique=False)
    submite= db.Column(db.String(70), unique=False)