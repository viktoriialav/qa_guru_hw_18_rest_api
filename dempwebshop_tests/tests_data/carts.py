from dataclasses import dataclass

from dempwebshop_tests.tests_data.products import Product, product_4, product_31, product_72, product_28


@dataclass
class UserCart:
    products: list[tuple[Product, int], ...]


cart_1 = UserCart(products=[(product_72, 3)])

cart_2 = UserCart(products=[(product_4, 6), (product_31, 2), (product_28, 1)])

print(cart_1.products)
