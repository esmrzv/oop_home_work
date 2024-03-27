class Product:
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        else:
            return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, color, performance, model, amount_memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, color, country_of_origin, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
