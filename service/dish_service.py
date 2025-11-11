from repository.dish_repository import Dish_repository


class Dish_Service:
    dish_repository = Dish_repository()

    @classmethod
    def save(cls, dish):
        return cls.dish_repository.save(dish)

    @classmethod
    def update(cls, dish):
        return cls.dish_repository.update(dish)

    @classmethod
    def delete(cls, dish):
        return cls.dish_repository.delete(dish)

    @classmethod
    def find_by_name(cls,name):
        dish = cls.dish_repository.find_by_name(name)
        if dish:
            return dish
        else:
            raise ValueError("Dish not found")

    @classmethod
    def find_by_category(cls,category):
        dish = cls.dish_repository.find_by_category(category)
        if dish:
            return dish
        else:
            raise ValueError("Dish not found")

    @classmethod
    def find_by_available(cls,available):
        dish = cls.dish_repository.find_by_available(available)
        if dish:
            return dish
        else:
            raise ValueError("Dish not found")


    @classmethod
    def find_by_id(cls, dish_id):
        dish = cls.dish_repository.find_by_id(dish_id)
        if dish:
            return dish
        else:
            raise ValueError("Dish not found")


    @classmethod
    def get_all(cls):
        return cls.dish_repository.get_all()
