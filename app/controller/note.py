from flask import make_response, abort
from ..model import db
from ..model.people import Person
from ..model.note import Note, NoteSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp
    :return:                json list of all notes for all people
    """
    # Query the database for all the notes
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    # Serialize the list of notes from our data
    note_schema = NoteSchema(many=True, exclude=["person.notes"])
    data = note_schema.dump(notes).data
    return data
