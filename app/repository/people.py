from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


"""
These are the data to be handled and manipulated by the API in memory execution time.
They simulate data coming from the database.
"""
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}
