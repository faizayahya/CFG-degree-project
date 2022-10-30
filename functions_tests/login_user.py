import db_files.db_utils as db
from displays.menus import *
from displays.messages import *
import re
import sys


class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.logged_in = False
        self.playlist = None
        self.mood_score = None
        self.entry_done = False
        self.date = None

    @staticmethod
    def has_account():
        has_account_menu()
        try:
            account = input('').lower().strip()
            if account == "1" or account == 'yes' or account == 'y':
                return True
            elif account == "2" or account == 'no' or account == 'n':
                return False
            elif account == "3" or account == "q" or account == "quit":
                quit_msg()
                raise sys.exit()
            else:
                raise ValueError
        except ValueError:
            has_account_error_msg()
            User.has_account()

    def set_username(self):
        possible_username = input('Set a username:')
        try:
            if User.username_valid(possible_username):
                self.username = possible_username
                return self.username
            else:
                raise ValueError
        except ValueError:
            invalid_username_msg()
            self.set_username()

    @staticmethod
    def username_valid(possible_username):
        if len(possible_username) < 3 or len(possible_username) > 10 or not possible_username.isalnum():
            return False
        else:
            return True

    def set_password(self):
        possible_password = input('Set a password:')
        try:
            if User.password_valid(possible_password):
                self.password = possible_password
                return self.password
            else:
                raise ValueError
        except ValueError:
            invalid_password_msg()
            self.set_password()

    @staticmethod
    def password_valid(possible_password):
        if len(possible_password) < 4 or len(possible_password) > 15:
            return False
        else:
            return True

    def set_email(self):
        possible_email = input('Please write your email address:')
        try:
            if User.email_is_valid(possible_email):
                self.email = possible_email
                return self.email
            else:
                raise ValueError
        except ValueError:
            try_email_again_msg()
            self.set_email()

    @staticmethod
    def email_is_valid(email_entry):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email_entry):
            return False
        else:
            return True

    def wants_to_login(self):
        wants_to_login_menu()
        user_answer = input('')
        try:
            if user_answer == '1':
                return True
            elif user_answer == '2':
                quit_msg()
                return False
            else:
                raise ValueError
        except ValueError:
            wants_to_login_error_msg()
            self.wants_to_login()

    def login(self):
        try:
            self.username = input('Please enter your username:')
            self.password = input('Please enter your password:')
            account_authenticated = db.InAccountsTable.authenticate_login_in_db(self.username, self.password)
            if account_authenticated:
                self.logged_in = True
                return self.logged_in
            else:
                raise ValueError
        except ValueError:
            incorrect_password_msg()
            self.login()
        except IndexError:
            username_not_recognised_msg()
            self.login()

    def entry_made(self):
        if db.InPlaylistsTable.entry_made_check_db(self.username, self.date):
            return True
        else:
            return False

    @staticmethod
    def end_menu_choices():
        end_menu()
        user_answer = input('')
        try:
            if user_answer == '1':
                return True
            elif user_answer == '2':
                return False
            else:
                raise ValueError
        except ValueError:
            end_menu_choices_error_msg()
            User.end_menu_choices()

    def logout(self):
        self.username = None
        self.password = None
        self.email = None
        self.logged_in = False
        self.playlist = None
        self.mood_score = None
        self.entry_done = False
        self.date = None
        quit_msg()
