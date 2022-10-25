import builtins
from unittest import TestCase
from unittest.mock import Mock
from login_user import User


# in this file we test: register, login, entry_made, logout, email_is_valid

class TestRegister(TestCase):
    pass
    # I don't know how to test the register function, will probably need to mock


class TestValidEmail(TestCase):
    def test_invalid_email_returns_false(self):
        pass

    def test_valid_email_returns_true(self):
        pass


class TestLoginFunction(TestCase):
    pass
# will probably need to mock


class TestEntryMadeFunction(TestCase):
    pass
# will probably need to mock


class TestLogoutFunction:
    pass
# will probably need to mock
