import builtins
from unittest import TestCase
from unittest.mock import Mock, patch
from functions_tests.login_user import *


class TestLoginFunction(TestCase):
    @patch("db_files.db_utils.InAccountsTable.authenticate_login_in_db")
    def test_password_matches_username(self, mock_authenticate):
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['gooduser', 'goodpword']
        a_user = User()
        mock_authenticate.return_value = True
        expected = True
        # act
        result = a_user.login()
        # assert
        self.assertEqual(expected, result)

    @patch("db_files.db_utils.InAccountsTable.authenticate_login_in_db", return_value=False)
    @patch('builtins.input', return_value=["gooduser", "badpword"])
    def test_wrong_value_throws_value_error(self, mock_authenticate, mocked_value):
        with self.assertRaises(ValueError):
            a_user = User()
            a_user.login()


class TestEntryMadeFunction(TestCase):
    @patch("db_files.db_utils.InPlaylistsTable.entry_made_check_db")
    def test_entry_made(self, mock_entry_made_check):
        mock_entry_made_check.return_value = True
        a_user = User()
        self.assertTrue(a_user.entry_made())

    @patch("db_files.db_utils.InPlaylistsTable.entry_made_check_db")
    def test_entry_not_made(self, mock_entry_made_check):
        mock_entry_made_check.return_value = False
        a_user = User()
        self.assertFalse(a_user.entry_made())


class TestLogoutFunction(TestCase):

    @patch("functions_tests.login_user.User.end_menu_choices")
    def test_logout(self, mock_end_menu_choice):
        mock_end_menu_choice.return_value = False
        a_user = User()
        expected = None
        result = a_user.logout()

        self.assertEqual(expected, result)
