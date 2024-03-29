from ..model import db
from ..model.people import Person, PersonSchema
from ..model.note import Note


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return: json string of list of people
    """

    # Create the list of people from our data
    people = Person.query.order_by(Person.lname).all()

    # Serialize the data for the response
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people).data


def read_one(person_id):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param person_id: Id of person to find
    :return:          person matching last name
    """

    person = (
        Person.query.filter(Person.person_id == person_id)
        .outerjoin(Note)
        .one_or_none()
    )

    person_schema = PersonSchema()
    return person_schema.dump(person).data


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """

    lname = person.get("lname", None)
    fname = person.get("fname", None)

    existing_person = Person.query \
        .filter(Person.fname == fname) \
        .filter(Person.lname == lname) \
        .one_or_none()

    if existing_person is not None:
        return False
    else:
        # Create a person instance using the schema and the passed-in person
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session).data

        # Add the person to the database
        db.session.add(new_person)
        db.session.commit()

        # Serialize and return the newly created person in the response
    return schema.dump(new_person).data


def update(person_id, person):
    """
    This function updates an existing person in the people structure

    :param person_id: Id of the person to update in the people structure
    :param person:    person to update
    :return:          updated person structure
    """

    # Get the person requested from the db into session
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()

    if update_person is None:
        return False
    else:
        # turn the passed in person into a db object
        schema = PersonSchema()
        upd = schema.load(person, session=db.session).data

        # Set the id to the person we want to update
        upd.id = update_person.person_id

        # merge the new object into the old and commit it to the db
        db.session.merge(upd)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person).data

        return data


def delete(person_id):
    """
    This function deletes a person from the people structure

    :param person_id: Id of the person to delete
    :return:          200 on successful delete, 404 if not found
    """

    # Get the person requested
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is None:
        return
    else:
        db.session.delete(person)
        db.session.commit()
        return True
