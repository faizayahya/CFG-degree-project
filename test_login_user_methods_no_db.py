import builtins
from unittest import TestCase
from unittest.mock import Mock, patch
from functions_tests.login_user import User

# TODO tests for has_account edge cases / invalid entries --> raises ValueError then returns User.has_account
#   "i have an account", "my answer is yes", "qu" "one" "two" "three" "12" "one" "two" "3."

# TODO test for wants_to_login  edge cases / invalid entries --> raises ValueError then returns uUser.wants_to_login
#   (when something other than 1 or 2 or 3, "one" "two")

# TODO tests for end_menu_choices edge cases / invalid entries --> ValueError, returns a function User.end_menu_choices
#   (when something other than 1 or 2 "one" "two" "logout")

# TODO tests for set email/password/username --> returns itself

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

    def test__input_quit_exits(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["quit"]
            User.has_account()

    def test_input_q_exits(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["q"]
            User.has_account()

    # def test_invalid_input(self):
    #     with self.assertRaises(ValueError):
    #         builtins.input = Mock()
    #         builtins.input.side_effect = [""]
    #         User.has_account()


class TestUsernameValid(TestCase):
    def test_valid_username_true(self):
        self.assertTrue(User.username_valid("username"))

    def test_long_username_false(self):
        self.assertFalse(User.username_valid("usernameusernameusernameusername"))

    def test_short_username_false(self):
        self.assertFalse(User.username_valid("use"))

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
    @patch("functions_tests.login_user.User.username_valid")
    def test_setting_valid_email_updates_user_attribute(self, mock_valid_username):  # Valid Input
        builtins.input = Mock()
        builtins.input.side_effect = ['username']
        mock_valid_username.return_value = True
        a_user = User()
        expected = "username"
        result = a_user.set_username()

        self.assertEqual(expected, result)

    def test_for_invalid_username(self):
        pass
class TestSetPassword(TestCase):
    @patch("functions_tests.login_user.User.password_valid")
    def test_setting_valid_email_updates_user_attribute(self, mock_valid_password):  # Valid Input
        builtins.input = Mock()
        builtins.input.side_effect = ['password']
        mock_valid_password.return_value = True
        a_user = User()
        expected = "password"
        result = a_user.set_password()

        self.assertEqual(expected, result)

    def test_for_invalid_pword(self):
        pass

class TestSetEmail(TestCase):
    @patch("functions_tests.login_user.User.email_is_valid")
    def test_setting_valid_email_updates_user_attribute(self, mock_valid_email):  # Valid Input
        builtins.input = Mock()
        builtins.input.side_effect = ['email@email.com']
        mock_valid_email.return_value = True
        a_user = User()
        expected = "email@email.com"
        result = a_user.set_email()

        self.assertEqual(expected, result)

    def test_for_invalid_email(self):
        pass


class TestWantsToLoginFunction(TestCase):
    def test_input_1_true(self):  # Valid Input
        a_user = User()
        with patch("builtins.input", side_effect=["1"]):
            self.assertTrue(User.wants_to_login(a_user))

    def test_input_2_false(self):  # Valid Input
        a_user = User()
        with patch("builtins.input", side_effect=["2"]):
            self.assertTrue(User.wants_to_login(a_user))


    #def test_wants_to_login_returns_itself_for_empty_string(self):  # Invalid Input
        # a_user = User()
        #
        # builtins.input = Mock()
        # builtins.input.side_effect = [""]
        #
        # User.wants_to_login(a_user)
        #
        # self.assertRaises(ValueError)


class TestEndMenuChoices(TestCase):

    # def test_input_1_true(self):  # Valid Input
    #     with patch("builtins.input", side_effect=["1"]):
    #         self.assertFalse(User.end_menu_choices())

    def test_input_2_false(self):
        with patch("builtins.input", side_effect=["2"]):
            self.assertFalse(User.end_menu_choices())

    def test_end_menu_choices_returns_itself_for_invalid_input(self):  # Value Error then returns User.end_menu_choices()
        pass

    # def test_end_menu_choices_returns_itself_for_empty_string(self):  # Value Error then returns User.end_menu_choices()
    #     pass
