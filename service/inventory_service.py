from repository.inventory_repository import Inventory_repository


class Inventory_Service:
    inventory_repository = Inventory_repository()

    @classmethod
    def save(cls, inventory):
        return cls.inventory_repository.save(inventory)

    @classmethod
    def update(cls, inventory):
        return cls.inventory_repository.update(inventory)

    @classmethod
    def delete(cls, inventory):
        return cls.inventory_repository.delete(inventory)

    @classmethod
    def find_by_name(cls,name):
        inventory = cls.inventory_repository.find_by_name(name)
        if inventory:
            return inventory
        else:
            raise ValueError("Inventory not found")

    @classmethod
    def find_by_location(cls, location):
        inventory = cls.inventory_repository.find_by_location(location)
        if inventory:
            return inventory
        else:
            raise ValueError("Inventory not found")


    @classmethod
    def find_by_id(cls, id):
        inventory = cls.inventory_repository.find_by_id(id)
        if inventory:
            return inventory
        else:
            raise ValueError("Inventory not found")



    @classmethod
    def get_all(cls):
        return cls.inventory_repository.get_all()
