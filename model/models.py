# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class ItMitarbeiter(db.Model):
    __tablename__ = 'it_mitarbeiter'

    ITid = db.Column(db.Integer, primary_key=True, unique=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(32))
    address = db.Column(db.String(32))
    birth_date = db.Column(db.Date)



class Programme(db.Model):
    __tablename__ = 'programme'

    pgID = db.Column(db.Integer, primary_key=True, unique=True)
    designation = db.Column(db.String(32))
    developer = db.Column(db.String(64))
    last_update = db.Column(db.Date)
    publication_date = db.Column(db.Date)



class Programmesevr(db.Model):
    __tablename__ = 'programmesevr'

    PgSrvID = db.Column(db.Integer, primary_key=True, unique=True)
    drID = db.Column(db.ForeignKey('servr.drID'), index=True)
    pgID = db.Column(db.ForeignKey('programme.pgID'), index=True)

    servr = db.relationship('Servr', primaryjoin='Programmesevr.drID == Servr.drID', backref='programmesevrs')
    programme = db.relationship('Programme', primaryjoin='Programmesevr.pgID == Programme.pgID', backref='programmesevrs')



class Servr(db.Model):
    __tablename__ = 'servr'

    drID = db.Column(db.Integer, primary_key=True, unique=True)
    designation = db.Column(db.String(128))
    location = db.Column(db.String(64))
    Marke = db.Column(db.String(32))
    ITid = db.Column(db.ForeignKey('it_mitarbeiter.ITid'), index=True)

    it_mitarbeiter = db.relationship('ItMitarbeiter', primaryjoin='Servr.ITid == ItMitarbeiter.ITid', backref='servrs')
