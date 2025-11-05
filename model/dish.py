class Dish():
    def __init__(self,id, name,quatity, price, category, available, ingredients):
        self.id =id
        self.name = name
        self.quatity = quatity
        self.price = price
        self.category = category
        self.available = available
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.name, self.quatity, self.price, self.category, self.available, self.ingredients))



    def check_availability(dish):
        if dish.available>0:
            return True
