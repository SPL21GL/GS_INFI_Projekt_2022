from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Server(db.Model):
    __tablename__ = 'Server'

    drID = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(50), nullable=False)
    Marke = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    IT_mitarbeiter = db.relationship('IT_mitarbeiter', primaryjoin='Server.ITid == IT_mitarbeiter.ITid', backref='Server')

class IT_mitarbeiter(db.Model):
    __tablename__ = 'Mitarbeiter'

    ITid = db.Column(db.Integer, primary_key=True)
    las_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.String(50), nullable=False)

    
