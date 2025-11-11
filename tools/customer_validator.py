import re

def first_name_validator(first_name):
    if not(type(first_name) == str and re.match(r"^[a-z]{2,20}$",first_name)):
        raise ValueError("invalid firstname!!")

def last_name_validator(last_name):
        if not (type(last_name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", last_name)):
            raise ValueError("Invalid last_name !!!")
        else:
            return last_name


def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^[0-9]{7,14}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number