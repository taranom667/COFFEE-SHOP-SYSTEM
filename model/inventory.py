from tools.dish_validator import name_validator
from tools.inventory_validator import location_validator, capacity_validator


class Inventory:
    def __init__(self, id, name, material, manager, location, capacity):
        self.id = id
        self.name = name
        self.material = material
        self.manager = manager
        self.location = location
        self.capacity = capacity
    '''def validate(self):
        name_validator(self.name)
        location_validator(self.location)
        capacity_validator(self.capacity)'''



    def add_material(self, material):
        pass

    def remove_material(material_id):
        pass

    def find_material(material_id):
        pass

    def get_location(material):
        pass

    def get_expiring_material(within_days):
       pass

    def update_stock(material_id, change):
        pass

    def get_total_value(material):
        pass

    def generate_report(Inventory_id):
        pass



    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.name, self.material, self.manager, self.location, self.capacity))
