from enum import Enum


class ReturnMessage(Enum):
    GET_MESSAGE = "The Person with ID {person_id} not found."
    POST_SUCCESS_MESSAGE = "{lname} successfully created."
    POST_FAIL_MESSAGE = "Person with last name {lname} already exists."
    PUT_SUCCESS_FULL = "{lname} successfully updated."
    DELETED_SUCCESS_FULL = "{person_id} successfully deleted."
    NOT_FOUND_MESSAGE = "The Person with ID {person_id} not found."
