from collections import defaultdict
from product import Product

class ShoppingCart:
    def __init__(self):
        self.product = defaultdict(lambda: defaultdict(int))

    def add_product(self, product, quantity=1):
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, product, quantity=1):
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.product[sku] == 0:
            del self.products[sku]