from tools.rawmaterial_validator import  *
class Raw_material:
    def __init__(self, id, name, category, unit, quantity, price, purchase_date, expiry_date, location):
        self.id = id
        self.name = name
        self.category = category
        self.unit = unit
        self.quantity = quantity
        self.price = price
        self.purchase_date = purchase_date
        self.expiry_date = expiry_date
        self.location = location

    def validate(self):
            name_validator(self.name)
            category_validator(self.category)
            unit_validator(self.unit)
            price_validator(self.price)
            quantity_validator(self.quantity)
            price_validator(self.price)
            location_validator(self.location)

    def __repr__(self):
            return f"{self.__dict__}"

    def to_tuple(self):
            return tuple((self.id, self.name, self.category, self.unit, self.quantity,self.price, self.purchase_date, self.expiry_date, self.location))
