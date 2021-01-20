import pytest

pytestmark = [pytest.mark.abc, pytest.mark.slow]

@pytest.fixture(scope="module")
def my_setup():
    print()
    print(">>> setup <<<")
    return {'id': 20, 'name': 'Tom'}

@pytest.mark.xyz
def test_login_page_valid_user(my_setup):
    print("test1")


@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print("test2")
    print("Name: {}".format(my_setup.get('name')))
    pass

