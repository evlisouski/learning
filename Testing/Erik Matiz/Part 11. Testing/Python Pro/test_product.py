import unittest
from product import *


class ProductTestCace(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = "SHOES"
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

if __name__ == '__main__':
    unittest.main()
