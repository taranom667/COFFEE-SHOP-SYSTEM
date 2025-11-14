import re

def total_price_validator(total_price):
        if not(type(total_price) == int and total_price>0):
         raise ValueError("invalid firstname!!")
        else:
            return total_price

def payment_type_validator(payment_type):
        if not (type(payment_type) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", payment_type)):
            raise ValueError("Invalid payment_type !!!")
        else:
            return payment_type



def status_validator(status):
        if not (type(status) == str and re.match(r"^(paid|unpaid)$", status)):
            raise ValueError("Invalid status !!!")
        else:
            return status



'''
def datetime_validator(datetime):
    if not (type(datetime) == str and re.match(r"^[0-9]{7,14}$", datetime)):
        raise ValueError("Invalid datetime !!!")
    else:
        return datetime'''