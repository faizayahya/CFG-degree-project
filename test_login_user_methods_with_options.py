import builtins
from unittest import TestCase
from unittest.mock import Mock, patch
from functions_tests.login_user import User


# in this file, we are testing the following functions: has_account, wants_to_login, end_menu_choices
# These functions all rely on user inputs
# we are testing that those inputs return the expected results

# TODO tests for has_account edge cases / invalid entries --> raises ValueError then returns User.has_account
#   "i have an account", "my answer is yes", "qu" "one" "two" "three" "12" "one" "two" "3."

# TODO test for wants_to_login  edge cases / invalid entries --> raises ValueError then returns uUser.wants_to_login
#   (when something other than 1 or 2 or 3, "one" "two")

# TODO tests for end_menu_choices edge cases / invalid entries --> ValueError, returns a function User.end_menu_choices
#   (when something other than 1 or 2 "one" "two" "logout")


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


class TestWantsToLoginFunction(TestCase):
    def test_input_1_true(self):  # Valid Input
        a_user = User()
        with patch("builtins.input", side_effect=["1"]):
            self.assertTrue(User.wants_to_login(a_user))

    def test_input_2_false(self):  # Valid Input
        a_user = User()
        with patch("builtins.input", side_effect=["2"]):
            self.assertTrue(User.wants_to_login(a_user))

    # def test_invalid_entry_returns_itself(self):  # Invalid Input
    #     a_user = User()
    #
    #     builtins.input = Mock()
    #     builtins.input.side_effect = ["one"]
    #
    #     User.wants_to_login(a_user)
    #
    #     self.assertRaises(ValueError)

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

    def test_end_menu_choices_returns_itself_for_empty_string(self):  # Value Error then returns User.end_menu_choices()
        pass

# TODO tests for end_menu_choices edge cases / invalid entries --> ValueError, returns a function User.end_menu_choices
#   (when something other than 1 or 2 "one" "two" "logout")
