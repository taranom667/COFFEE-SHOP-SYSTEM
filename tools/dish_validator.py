import re
#name, quantity,category,username,password,price):

def name_validator(name):
    if not(type(name) == str and re.match(r"^[a-z]{2,20}$",name)):
        raise ValueError("invalid firstname!!")

def quantity_validator(quantity):
        if not (type(quantity) == int and quantity>=0, quantity):
            raise ValueError("Invalid quantity !!!")
        else:
            return quantity


def price_validator(price):
    if not (type(price) == int and price>=0, price):
        raise ValueError("Invalid price !!!")
    else:
        return price

def category_validator(category):
        if not (type(category) == str and re.match(r"^(cakes|cupcakes|cookies|pies|moose|cheesecakes|hot coffe|cold coffee|desserts|tea|milkshakes|add ons|food|starters|snacks|none coffee|vegan breakfast|proteiny)$", category)):
            raise ValueError("Invalid category !!!")
        else:
            return category



def available_validator(username):
    if not (type(username) == bool ):
        raise ValueError("Invalid username !!!")
    else:
        return username


def ingredients_validator(password):
    if not (type(password) == str and re.match(r"^[0-9a-zA-Z@#$%^&+=\w]{8,200}$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password

