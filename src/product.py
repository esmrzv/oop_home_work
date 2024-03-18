class Product:
    name: str
    description: str
    price: float
    quantity: int
    products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        new_product = cls(name, description, price, quantity)
        cls.products.append(new_product)
        return new_product

    def __repr__(self):
        """Хранит в списках шаблон по заданию 13.2 - Задача 2"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
