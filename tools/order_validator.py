import re


# customer_name, last_name,total_price,username,password,order):

def customer_name_validator(customer_name):
    if not (type(customer_name) == str and re.match(r"^[a-z]{2,20}$", customer_name)):
        raise ValueError("invalid customername!!")


def status_validator(status):
    if not (type(status) == str and re.match(r"^(confrimed|processing|in transit|ready|delivered|cancel)$", status)):
        raise ValueError("Invalid status !!!")
    else:
        return status


def total_price_validator(total_price):
    if not (type(total_price) == int and total_price > 0):
        raise ValueError("Invalid total_price !!!")
    else:
        return total_price


'''def datetme_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^[0-9]{7,14}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_numberv'''
