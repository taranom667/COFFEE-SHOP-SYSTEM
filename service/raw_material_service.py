from repository.Rawmaterial_repository import Raw_material_repository


class Raw_material_Service:
    raw_material_repository = Raw_material_repository()

    @classmethod
    def save(cls, raw_material):
        return cls.raw_material_repository.save(raw_material)

    @classmethod
    def update(cls, raw_material):
        return cls.raw_material_repository.update(raw_material)

    @classmethod
    def delete(cls, raw_material):
        return cls.raw_material_repository.delete(raw_material)

    @classmethod
    def find_by_name(cls,name):
        raw_material = cls.raw_material_repository.find_by_name(name)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")

    @classmethod
    def find_by_category(cls, category):
        raw_material = cls.raw_material_repository.find_by_category(category)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")

    @classmethod
    def find_by_quantity(cls, quantity):
        raw_material = cls.raw_material_repository.find_by_quantity(quantity)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")

    @classmethod
    def find_by_purchase_date(cls, purchase_date):
        raw_material = cls.raw_material_repository.find_by_purchase_date(purchase_date)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")

    @classmethod
    def find_by_id(cls, id):
        raw_material = cls.raw_material_repository.find_by_id(id)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")


    @classmethod
    def find_by_expiry_date(cls, expiry_date):
        raw_material = cls.raw_material_repository.find_by_expiry_date(expiry_date)
        if raw_material:
            return raw_material
        else:
            raise ValueError("Raw_material not found")


    @classmethod
    def get_all(cls):
        return cls.raw_material_repository.get_all()
