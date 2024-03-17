class Category:
    all_quantity_category = 0
    all_unique_product = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.all_quantity_category += 1

        Category.all_unique_product += len(self.products)



