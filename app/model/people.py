from datetime import datetime
from model import (db, ma)


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
