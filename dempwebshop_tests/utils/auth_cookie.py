import os

import allure
import dotenv
import requests
from selene import browser

from dempwebshop_tests.utils.data import endpoint_log_in, BASE_URL


def get_auth_cookie():
    dotenv.load_dotenv()
    with allure.step('Get cookie from API'):
        response = requests.post(url=f'{BASE_URL}{endpoint_log_in}',
                                 data={'Email': os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD'),
                                       'RememberMe': False},
                                 allow_redirects=False)
    return response.cookies.get('NOPCOMMERCE.AUTH')


def add_auth_cookie():
    with allure.step('Add authorization cookie'):
        browser.open(BASE_URL)
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': get_auth_cookie()})
        browser.open(BASE_URL)
