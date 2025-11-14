from tools.dish_validator import name_validator, quantity_validator, price_validator, category_validator, \
    available_validator, ingredients_validator


class Dish():
    def __init__(self,id, name,quantity, price, category, available, ingredients):
        self.id =id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.available = available
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.name, self.quantity, self.price, self.category, self.available, self.ingredients))

    def validate(self):
     name_validator(self.name)
     quantity_validator(self.quantity)
     price_validator(self.price)
     category_validator(self.category)
     available_validator(self.available)
     ingredients_validator((self.ingredients))


    def check_availability(dish):
        if dish.available>0:
            return True
