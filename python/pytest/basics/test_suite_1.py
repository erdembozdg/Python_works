import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
def test_login_page_valid_user():
    pass


@pytest.mark.regression
def test_login_page_wrong_password():
    pass
    # assert 1==2, 'eeeeee'

