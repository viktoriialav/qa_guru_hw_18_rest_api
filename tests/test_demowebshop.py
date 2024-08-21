import allure
from allure_commons.types import Severity

from dempwebshop_tests.pages.cart_page import CartPage
from dempwebshop_tests.tests_data.carts import cart_1, cart_2


@allure.feature('Test Demo Web Shop Cart')
@allure.severity(severity_level=Severity.CRITICAL)
@allure.label('owner', 'Viktoriia Lavrova')
class TestCart:
    def test_add_one_type_of_product_to_cart(self):
        # GIVEN
        cart = CartPage()
        cart.is_empty()

        # WHEN
        total_price, total_amount = cart.add_all_products_to_cart_with_api(cart_1)

        # THEN
        cart.open()
        cart.should_have_special_number(total_amount)
        cart.should_have_total_price(total_price)

    def test_add_some_types_of_products_to_cart(self):
        # GIVEN
        cart = CartPage()
        cart.is_empty()

        # WHEN
        total_price, total_amount = cart.add_all_products_to_cart_with_api(cart_2)

        # THEN
        cart.open()
        cart.should_have_special_number(total_amount)
        cart.should_have_total_price(total_price)
