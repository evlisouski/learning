import unittest

from cart import ShoppingCart
from product import Product


class ShopingCartTestCase(unittest.TestCase):
    def test_add_and_remove_product(self):
        cart = ShoppingCart()

        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertEqual({}, cart.products)
