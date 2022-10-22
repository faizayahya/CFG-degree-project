import builtins
from unittest import TestCase
from unittest.mock import Mock
from login_user import User
# in this file, we are testing the following functions: has_account, wants_to_login, end_menu_choices
# These functions all rely on user inputs
# we are testing that those inputs return the expected results

# TODO tests for has_account for the input 3/q/quit --> difficult because it returns sys.exit

# TODO tests for has_account edge cases / invalid entries --> raises ValueError then returns User.has_account
#   "i have an account", "my answer is yes", "qu" "one" "two" "three" "12" "one" "two" "3."

# TODO test for wants_to_login where input == 2 --> returns User.register

# TODO test for wants_to_login  edge cases / invalid entries --> raises ValueError then returns uUser.wants_to_login
#   (when something other than 1 or 2 or 3, "one" "two")

# TODO tests for end_menu_choices edge cases / invalid entries --> ValueError, returns a function User.end_menu_choices
#   (when something other than 1 or 2 "one" "two" "logout")


class TestHasAccountFunction(TestCase):
    def test_has_account_returns_true_input_1(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['1']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, True)

    def test_has_account_returns_true_input_yes(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['YEs']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, True)

    def test_has_account_returns_true_input_yes_capital_y(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['y']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, True)

    def test_has_account_returns_false_input_2(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['2']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, False)

    def test_has_account_returns_false_input_no(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['no']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, False)

    def test_has_account_returns_false_input_no_capital_n(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['No']
        builtins.print = Mock()
        # act
        result = User.has_account()
        # assert
        self.assertIs(result, False)

    def test_has_account_exits_input_3(self):
        pass

    def test_has_account_exits_input_quit(self):
        pass

    def test_has_account_exits_input_q(self):
        pass

    def test_has_account_invalid_input(self): # Value Error then returns User.has_account()
        pass
    # do several or all of the following for invalid inputs:
        # edge cases = "" "qu" "one" "two" "three" "12" "one" "two" "3."
        # completely invalid inputs = "i have an account", "my answer is yes"


class TestWantsToLoginFunction(TestCase):
    def test_wants_to_login_returns_true_input_1(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['1']
        builtins.print = Mock()
        a_user = User()
        # act
        result = User.wants_to_login(a_user)
        # assert
        self.assertIs(result, True)

    def test_wants_to_login_returns_register_method_input_2(self): # Valid Input returns User.register()
        pass
# TODO test for wants_to_login where input == 2 --> returns User.register

    def test_wants_to_login_returns_false_input_3(self):  # Valid Input
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['3']
        builtins.print = Mock()
        a_user = User()
        # act
        result = User.wants_to_login(a_user)
        # assert
        self.assertIs(result, False)

# TODO test for wants_to_login edge cases / invalid entries --> raises ValueError then returns User.wants_to_login
#   (when something other than 1 or 2 or 3, "one" "two" ""

    def test_wants_to_login_returns_itself_for_invalid_entry(self): # Value Error then returns User.wants_to_login()
        pass

    def test_wants_to_login_returns_itself_for_empty_string(self): # Value Error then returns User.wants_to_login()
        pass


class TestEndMenuChoices(TestCase):

    # def test_end_menu_choices_returns_true_input_1(self):  # Valid Input
    #     # setup
    #     builtins.input = Mock()
    #     builtins.input.side_effect = ['1']
    #     builtins.print = Mock()
    #     # act
    #     result = User.end_menu_choices()
    #     # assert
    #     self.assertIs(result, True)

    def test_end_menu_choices_returns_false_input_2(self):
        # setup
        builtins.input = Mock()
        builtins.input.side_effect = ['2']
        builtins.print = Mock()
        # act
        result = User.end_menu_choices()
        # assert
        self.assertIs(result, False)

    def test_end_menu_choices_returns_itself_for_invalid_input(self): # Value Error then returns User.end_menu_choices()
        pass

    def test_end_menu_choices_returns_itself_for_empty_string(self): # Value Error then returns User.end_menu_choices()
        pass

# TODO tests for end_menu_choices edge cases / invalid entries --> ValueError, returns a function User.end_menu_choices
#   (when something other than 1 or 2 "one" "two" "logout")