import re

def rider_validator(first_name):
    if not(type(first_name) == str and re.match(r"^[a-z\s]{2,30}$",first_name)):
        raise ValueError("invalid rider name!!")


def status_validator(role):
        if not (type(role) == str and re.match(r"^(order placed|label pending|in transit|out pf delivery|delivered)$", role)):
            raise ValueError("Invalid role !!!")
        else:
            return role



def address_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z0-9\s\w]{3,30}$", username)):
        raise ValueError("Invalid address !!!")
    else:
        return username

