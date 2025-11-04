class Dish():
    def __init__(self, dish_id, name, number, price, category, available, ingredients):
        self.dish_id = dish_id
        self.name = name
        self.number = number
        self.price = price
        self.category = category
        self.available = available
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.dish_id, self.name, self.number, self.price, self.category, self.available, self.ingredients))
