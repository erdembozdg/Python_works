import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
class TestCheckout(object):

    def test_checkout_as_guest(self):
        pass

    def test_checkout_with_existing_user(self):
        pass