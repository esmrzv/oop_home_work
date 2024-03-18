

class Category:
    all_quantity_category = 0
    all_unique_product = 0
    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.all_quantity_category += 1

        Category.all_unique_product += len(self.__products)

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    @property
    def __str__(self):
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity}шт")
        return products_list


