import pytest
from selene import browser

from dempwebshop_tests.utils.auth_cookie import get_auth_cookie, add_auth_cookie


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    add_auth_cookie()

    yield browser

    browser.quit()


