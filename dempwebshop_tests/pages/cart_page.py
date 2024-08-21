import allure
import requests
from selene import browser, be, have

from dempwebshop_tests.tests_data.carts import UserCart
from dempwebshop_tests.tests_data.products import Product
from dempwebshop_tests.utils.auth_cookie import get_auth_cookie
from dempwebshop_tests.utils.data import BASE_URL, endpoint_add_to_cart
from dempwebshop_tests.utils.attach_log import request_attaching_and_logging


class CartPage:
    def open(self):
        with allure.step('Open the personal cart'):
            browser.element('#topcartlink').click()

    def delete_all_products(self):
        with allure.step('Delete all products from the cart'):
            delete_flags = browser.all('[name=removefromcart]')
            for item in delete_flags:
                item.click()
            browser.element('[name=updatecart]').click()

    def is_empty(self):
        self.open()
        if not browser.element('[name=updatecart]').matching(be.hidden):
            self.delete_all_products()

    def add_one_product_to_cart_with_api(self, item: Product, amount=1):
        with allure.step(f'Add {amount} product(s) #{item.number} into the cart'):
            data = item.payload
            data[f'addtocart_{item.number}.EnteredQuantity'] = str(amount)
            response = requests.request(method='POST', url=f'{BASE_URL}{endpoint_add_to_cart}{item.number}/1',
                                        data=data, cookies={'NOPCOMMERCE.AUTH': get_auth_cookie()})

            request_attaching_and_logging(response)
        return response

    def add_all_products_to_cart_with_api(self, items: UserCart):
        total_price = 0
        total_amount = 0
        for product in items.products:
            self.add_one_product_to_cart_with_api(item=product[0], amount=product[1])
            total_price += product[0].price * product[1]
            total_amount += product[1]
        return total_price, total_amount

    def should_have_special_number(self, value):
        with allure.step('Verify amount of all products'):
            browser.element('.cart-qty').should(have.exact_text(f'({value})'))

    def should_have_total_price(self, value):
        with allure.step('Verify total price of products'):
            browser.element('.order-total').should(have.exact_text(f'{value:.2f}'))
