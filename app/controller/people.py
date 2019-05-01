from flask import make_response, abort
from repository import people as people


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return: json string of list of people
    """
    # Create the list of people from our data
    return [people.PEOPLE[key] for key in sorted(people.PEOPLE.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people
    :param lname:   last name of person to find
    :return:        person matching last name
    """

    if lname not in people.PEOPLE:
        return None

    # Does the person exist in people?
    else:
        person = people.PEOPLE.get(lname)

    return person


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """

    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in people.PEOPLE and lname is not None:
        people.PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": people.get_timestamp(),
        }
        return True
    else:
        return False


def update(lname, person):
    """
    This function updates an existing person in the people structure
    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    if lname not in people.PEOPLE:
        return None

    # Does the person exist in people?
    else:
        people.PEOPLE[lname]["fname"] = person.get("fname")
        people.PEOPLE[lname]["timestamp"] = people.get_timestamp()

    return people.PEOPLE[lname]


def delete(lname):
    """
    This function deletes a person from the people structure
    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lname in people.PEOPLE:
        del people.PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
