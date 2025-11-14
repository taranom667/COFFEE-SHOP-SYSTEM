import re


# name, last_name,role,username,password,location):

def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-z]{2,20}$", name)):
        raise ValueError("invalid firstname!!")


def location_validator(location):
    if not (type(location) == str and re.match(r"^[a-zA-Z0-9\d\w\s]{2,120}$", location)):
        raise ValueError("Invalid location !!!")
    else:
        return location


def capacity_validator(capacity):
    if not (type(capacity) == str and re.match(r"^[a-zA-Z0-9\d\w\s]{2,120}$", capacity)):
        raise ValueError("Invalid capacity !!!")
    else:
        return capacity
