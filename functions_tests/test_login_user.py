import builtins
from unittest import TestCase
from unittest.mock import Mock, patch
from functions_tests.login_user import User

# TESTS FOR ALL FUNCTIONS IN THE login_user.py FILE


class TestHasAccountFunction(TestCase):
    def test_input_1_true(self):
        with patch("builtins.input", side_effect=["1"]):
            self.assertTrue(User.has_account())

    def test_input_yes_true(self):
        with patch("builtins.input", side_effect=["YEs"]):
            self.assertTrue(User.has_account())

    def test_input_yes_capital_y_true(self):
        with patch("builtins.input", side_effect=["y"]):
            self.assertTrue(User.has_account())

    def test_input_2_false(self):
        with patch("builtins.input", side_effect=["2"]):
            self.assertFalse(User.has_account())

    def test_input_no_false(self):
        with patch("builtins.input", side_effect=["no"]):
            self.assertFalse(User.has_account())

    def test_input_no_capital_n_false(self):
        with patch("builtins.input", side_effect=["No"]):
            self.assertFalse(User.has_account())

    def test_input_3_exits(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["3"]
            User.has_account()

    def test_input_quit_exits(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["quit"]
            User.has_account()

    def test_input_q_exits(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["q"]
            User.has_account()

    @patch('builtins.input', side_effect=["p"])
    def test_invalid_input_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            User.has_account()

    @patch('builtins.input', side_effect=[""])
    def test_invalid_input_then_valid_input_no_error(self, mocked_invalid_input):
        with patch("builtins.input", return_value="1"):
            User.has_account()
            self.assertTrue(User.has_account())


class TestUsernameValid(TestCase):
    def test_valid_username_true(self):
        self.assertTrue(User.username_valid("username"))

    def test_long_username_false(self):
        self.assertFalse(User.username_valid("usernameusernameusernameusername"))

    def test_short_username_false(self):
        self.assertFalse(User.username_valid("us"))

    def test_special_char_username_false(self):
        self.assertFalse(User.username_valid("username!"))

    def test_empty_username_false(self):
        self.assertFalse(User.username_valid(""))


class TestPasswordValid(TestCase):
    def test_valid_password_true(self):
        self.assertTrue(User.password_valid("password"))

    def test_long_password_false(self):
        self.assertFalse(User.password_valid("passwordpasswordpasswordpassword"))

    def test_short_password_false(self):
        self.assertFalse(User.password_valid("pas"))

    def test_empty_password_false(self):
        self.assertFalse(User.password_valid(""))


class TestEmailValid(TestCase):
    def test_valid_email_true(self):
        self.assertTrue(User.email_is_valid("my_valid_email@email.com"))

    def test_invalid_email_false(self):
        self.assertFalse(User.email_is_valid("my_invalid_email_@emailcom"))

    def test_no_at_sign_email_false(self):
        self.assertFalse(User.email_is_valid("my_invalid_emailemail.com"))

    def test_empty_email_false(self):
        self.assertFalse(User.email_is_valid(""))


class TestSetUsername(TestCase):
    @patch('builtins.input', return_value='username')
    def test_setting_valid_username_updates_user_attribute(self, mock_valid_username):  # Valid Input
        expected = "username"
        a_user = User()
        result = a_user.set_username()

        self.assertEqual(expected, result)

    @patch('builtins.input', side_effect=["p"])
    def test_invalid_username_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            a_user = User()
            a_user.set_username()


class TestSetPassword(TestCase):
    @patch('builtins.input', return_value='password')
    def test_setting_valid_email_updates_user_attribute(self, mock_valid_password):  # Valid Input
        expected = 'password'
        a_user = User()
        result = a_user.set_password()

        self.assertEqual(expected, result)

    @patch('builtins.input', side_effect=["p"])
    def test_invalid_password_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            a_user = User()
            a_user.set_password()


class TestSetEmail(TestCase):
    @patch('builtins.input', return_value="email@email.com")
    def test_setting_valid_email_updates_user_attribute(self, mock_valid_email):
        expected = "email@email.com"
        a_user = User()
        result = a_user.set_email()

        self.assertEqual(expected, result)

    @patch('builtins.input', side_effect=["eeeeee@eeee"])
    def test_invalid_email_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            a_user = User()
            a_user.set_email()


class TestWantsToLoginFunction(TestCase):
    def test_input_1_true(self):  # Valid Input
        with patch("builtins.input", side_effect=["1"]):
            a_user = User()
            self.assertTrue(a_user.wants_to_login())

    def test_input_2_false(self):  # Valid Input
        with patch("builtins.input", side_effect=["2"]):
            a_user = User()
            self.assertFalse(a_user.wants_to_login())

    @patch('builtins.input', side_effect=["3"])
    def test_invalid_input_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            a_user = User()
            a_user.wants_to_login()

    @patch('builtins.input', side_effect=["3"])
    def test_invalid_input_then_valid_input(self, mocked_invalid_input):
        with patch("builtins.input", return_value="2"):
            a_user = User()
            a_user.wants_to_login()
            self.assertFalse(a_user.wants_to_login())


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
    @patch('builtins.input', side_effect=["gooduser", "badpword"])
    def test_wrong_value_throws_error(self, mock_authenticate, mocked_value):
        with self.assertRaises(Exception):
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


class TestEndMenuChoices(TestCase):

    def test_input_1_true(self):  # Valid Input
        with patch("builtins.input", side_effect=["1"]):
            self.assertTrue(User.end_menu_choices())

    def test_input_2_false(self):
        with patch("builtins.input", side_effect=["2"]):
            self.assertFalse(User.end_menu_choices())

    @patch('builtins.input', side_effect=["3"])
    def test_invalid_input_throws_error(self, mocked_input):
        with self.assertRaises(Exception):
            User.end_menu_choices()

    @patch('builtins.input', side_effect=["3"])
    def test_invalid_input_then_valid_input(self, mocked_invalid_input):
        with patch("builtins.input", return_value="2"):
            User.end_menu_choices()
            self.assertFalse(User.end_menu_choices())


class TestLogoutFunction(TestCase):

    @patch("functions_tests.login_user.User.end_menu_choices")
    def test_logout(self, mock_end_menu_choice):
        mock_end_menu_choice.return_value = False
        a_user = User()
        expected = None
        result = a_user.logout()

        self.assertEqual(expected, result)

