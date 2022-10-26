import builtins
from unittest import TestCase, mock
from functions_tests.login_user import *
from db_files.db_utils import *


# todo  login invalid test case

class TestLoginFunction(TestCase):
    @mock.patch("db_files.db_utils.InAccountsTable.authenticate_login_in_db")
    def test_password_matches_username(self, mock_authenticate):
        # setup
        builtins.input = mock.Mock()
        builtins.input.side_effect = ['humi', 'humi1234']
        a_user = User()
        mock_authenticate.return_value = True
        expected = True
        # act
        result = User.login(a_user)
        # assert
        self.assertEqual(expected, result)

    # @mock.patch("db_files.db_utils.InAccountsTable.authenticate_login_in_db")
    # def test_incorrect_password(self, mock_authenticate):
    #     # setup
    #     builtins.input = mock.Mock()
    #     builtins.input.side_effect = ['humi', '1234']
    #     a_user = User()
    #     mock_authenticate.return_value = False
    #     expected = None
    #     # act
    #     result = User.login(a_user)
    #     # assert
    #     self.assertEqual(expected, result)


class TestEntryMadeFunction(TestCase):
    @mock.patch("db_files.db_utils.InPlaylistsTable.entry_made_check_db")
    def test_entry_made(self, mock_entry_made_check):
        mock_entry_made_check.return_value = True
        a_user = User()
        self.assertTrue(User.entry_made(a_user))

    @mock.patch("db_files.db_utils.InPlaylistsTable.entry_made_check_db")
    def test_entry_not_made(self, mock_entry_made_check):
        mock_entry_made_check.return_value = False
        a_user = User()
        self.assertFalse(User.entry_made(a_user))


class TestLogoutFunction(TestCase):

    @mock.patch("functions_tests.login_user.User.end_menu_choices")
    def test_logout(self, mock_end_menu_choice):
        mock_end_menu_choice.return_value = False
        a_user = User()
        expected = None
        result = User.logout(a_user)

        self.assertEqual(expected, result)
