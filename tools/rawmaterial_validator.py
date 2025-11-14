import re

def name_validator(name):
    if not(type(name) == str and re.match(r"^[a-z]{2,20}$",name)):
        raise ValueError("invalid name!!")

def category_validator(category):
        if not (type(category) == str and re.match(r"^$", category)):
            raise ValueError("Invalid category !!!")
        else:
            return category


def unit_validator(unit):
    pass
    return unit

def quantity_validator(quantity):
        if not (type(quantity) == int and quantity >= 0):
            raise ValueError("Invalid quantity !!!")
        else:
            return quantity



def price_validator(price):
    if not (type(price) == str and price >= 0):
        raise ValueError("Invalid price !!!")
    else:
        return price

'''
def purchase_date_validator(purchase_date):
    if not (type(purchase_date) == str ):
        raise ValueError("Invalid purchase_date !!!")
    else:
        return purchase_date

def expiry_date_validator(expiry_date):
    if not (type(expiry_date) == str ):
        raise ValueError("Invalid expiry_date !!!")
    else:
        return expiry_date
'''

def location_validator(location):
    if not (type(location) == str and re.match(r"^a-z]{2,100}$", location)):
        raise ValueError("Invalid location !!!")
    else:
        return location