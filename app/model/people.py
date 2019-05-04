from datetime import datetime
from model import db


class Person(db.Model):
    __tabename__ = 'person'
    person_id = db.column(db.Integer, primary_key=True)
    fname = db.column(db.String)
    lname = db.column(db.String)
    timestamp = db.column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
