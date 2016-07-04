__author__ = 'jayson_rodrigues'

import pytest
from Pages.registration import Register
from Pages.homepage import Homepage


register = Register()
homepage = Homepage()

@pytest.mark.nondestructive
def test_register(base_url, selenium):
    selenium.get(base_url)
    homepage.click_on_create_account(selenium)
    register.register(selenium)
