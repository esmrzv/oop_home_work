from src.product import Product


class Category:
    all_quantity_category = 0
    all_unique_product = 0
    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.all_quantity_category += 1

        Category.all_unique_product += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)

    @property
    def product_info(self):
        products_list = []
        for product in self.__products:
            products_list.append(str(product))
        return products_list

    def __str__(self):
        return f'{self.name}, колличество продуктов: {len(self)} шт'

    def __len__(self):
        num_product = 0
        for product in self.__products:
            num_product += product.quantity
        return num_product





