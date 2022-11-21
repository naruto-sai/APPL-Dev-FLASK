from datetime import datetime
from crud import db

class User(db.Model):  
    id =  db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(20), nullable=False)
    lastname=db.Column(db.String(20), nullable=False)
    designation=db.Column(db.String(60), nullable=False)
    email=db.Column(db.String(120), nullable=False)
    number=db.Column(db.Integer, unique=True, nullable=False)
    about=db.Column(db.String(200), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.firstname} {self.lastname}','{self.designation}','{self.email}','{self.number}','{self.about}','{self.date_posted}')"


