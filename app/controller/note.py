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


def read_one(person_id, note_id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person
    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    note = (
        Note.query.join(Person, Person.person_id == Note.person_id)
        .filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # Was a note found?
    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note).data
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {note_id}")


