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

        def update_quantity(amount):
            pass

        def is_expired(current_date):
            pass

        def days_to_expiry(current_date):
            pass

        def get_total_value():
            pass

        def display_info():
            pass

        def validate(self):
            pass

        def __repr__(self):
            return f"{self.__dict__}"

        def to_tuple(self):
            return tuple((self.id, self.name, self.category, self.unit, self.quantity,self.price, self.purchase_date, self.expiry_date, self.location))
