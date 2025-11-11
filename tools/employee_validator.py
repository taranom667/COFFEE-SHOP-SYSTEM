import re
#first_name, last_name,role,username,password,salary):

def first_name_validator(first_name):
    if not(type(first_name) == str and re.match(r"^[a-z]{2,20}$",first_name)):
        raise ValueError("invalid firstname!!")

def last_name_validator(last_name):
        if not (type(last_name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", last_name)):
            raise ValueError("Invalid last_name !!!")
        else:
            return last_name


def salary_validator(salary):
    if not (type(salary) == int and salary>0, salary):
        raise ValueError("Invalid salary !!!")
    else:
        return salary

def role_validator(role):
        if not (type(role) == str and re.match(r"^(manager|cashier|chef|courier|waiter)$", role)):
            raise ValueError("Invalid role !!!")
        else:
            return role



def username_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z0-9]{3,30}$", username)):
        raise ValueError("Invalid username !!!")
    else:
        return username


def password_validator(password):
    if not (type(password) == str and re.match(r"^[0-9a-zA-Z@#$%^&+=]{8,20}$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password

def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^[0-9]{7,14}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number