__author__ = 'jayson_rodrigues'

import pytest
from Pages.login import Login

login = Login()

@pytest.mark.nondestructive
def test_login(base_url, selenium):
    selenium.get(base_url)
    login.login(selenium)