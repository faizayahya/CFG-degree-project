import builtins
from unittest import TestCase, mock
from functions_tests.login_user import *
from db_files.db_utils import *


# in this file we test: login, entry_made, logout, email_is_valid


class TestValidEmail(TestCase):

    def test_valid_email_returns_true(self):
        self.assertTrue(User.email_is_valid("my_valid_email@email.com"))
        self.assertTrue(User.email_is_valid("myother.validemail@email.com"))

    def test_invalid_email_returns_false(self):
        self.assertFalse(User.email_is_valid("my_invalid_email_@emailcom"))

    def test__no_at_email_returns_false(self):
        self.assertFalse(User.email_is_valid("my_invalid_emailemail.com"))

    def test_empty_email_returns_false(self):
        self.assertFalse(User.email_is_valid(""))


class TestLoginFunction(TestCase):
    pass


# will probably need to mock


class TestEntryMadeFunction(TestCase):
    pass


# will probably need to mock


class TestLogoutFunction:
    pass
# will probably need to mock
