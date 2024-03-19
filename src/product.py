class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, __price, quantity):
        self.name = name
        self.description = description
        self.__price = self.price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Указана некорректная цена')
        else:
            self.__price = price

    @classmethod
    def create_product(cls, data):
        new_product = cls(**data)
        return new_product


def __repr__(self):
    """Хранит в списках шаблон по заданию 13.2 - Задача 2"""
    return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
