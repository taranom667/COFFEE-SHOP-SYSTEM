class Session:
    employee=None
    customer = None
    order = None
    dish = []
    payment = None

    @classmethod
    def add_order_item(cls, order_item):
        cls.order_items.append(order_item)