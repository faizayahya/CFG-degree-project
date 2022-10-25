import db_files.db_utils as db
from Menus.menus import Menus
from Messages.messages import Messages
import re
import sys


#               14 functions:

#               has_account
#               set_username
#               username_valid
#               set_password
#               password_valid
#               set_email
#               email_is_valid
#               account_exists_check
#               register
#               wants_to_login
#               login
#               entry_made
#               end_menu_choices
#               logout

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
        Menus.has_account_menu()
        try:
            account = input('').lower().strip()
            if account == "1" or account == 'yes' or account == 'y':
                return True
            elif account == "2" or account == 'no' or account == 'n':
                return False
            elif account == "3" or account == "q" or account == "quit":
                Messages.quit_msg()
                return sys.exit()
        except ValueError:
            Messages.has_account_error_msg()
            return User.has_account()

    def set_username(self):
        possible_username = input('Set a username:')
        if not User.username_valid(possible_username):
            return self.set_username()
        else:
            self.username = possible_username
            return self.username

    @staticmethod
    def username_valid(possible_username):
        if len(possible_username) < 3 or len(possible_username) > 10 or not possible_username.isalnum():
            Messages.invalid_username_msg()
            return False
        else:
            return True

    def set_password(self):
        possible_password = input('Set a password:')
        if not User.password_valid(possible_password):
            Messages.invalid_password_msg()
            return self.set_password()
        else:
            self.password = possible_password
            return self.password

    @staticmethod
    def password_valid(possible_password):
        if len(possible_password) < 4:
            Messages.invalid_password_msg()
            return False
        else:
            return True

    def set_email(self):
        possible_email = input('Please write your email address:')
        if not User.email_is_valid(possible_email):
            Messages.try_email_again_msg()
            return self.set_email()
        else:
            self.email = possible_email
            return self.email

    @staticmethod
    def email_is_valid(email_entry):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email_entry):
            return False
        else:
            return True

    def account_exists_check(self):
        account_exists = db.InAccountsTable.username_in_db_check(self.username)
        if account_exists:
            Messages.duplicate_username_msg()
            if self.wants_to_login():
                self.login()
            else:
                exit()

    def register(self):
        db.InAccountsTable.insert_new_user_to_db(self.set_username(), self.set_password(), self.set_email())
        Messages.new_account_success_msg()
        self.logged_in = True
        return self.logged_in

    def wants_to_login(self):
        Menus.wants_to_login_menu()
        user_answer = input('')
        try:
            if user_answer == '1':
                return True
            elif user_answer == '2':
                return self.register()
            elif user_answer == '3':
                Messages.quit_msg()
                return False
        except ValueError:
            print('Please enter 1 to Login, 2 to register with a different account, or 3 for Quit')
            return self.wants_to_login()

    def login(self):
        self.username = input('Please enter your username:')
        self.password = input('Please enter your password:')
        account_authenticated = db.InAccountsTable.authenticate_login_in_db(self.username, self.password)
        if account_authenticated:
            self.logged_in = True
        else:
            self.login()

    def entry_made(self):
        if db.InPlaylistsTable.entry_made_check_db(self.username, self.date):
            return True
        else:
            return False

    @staticmethod
    def end_menu_choices():
        Menus.end_menu()
        user_answer = input('')
        try:
            if user_answer == '1':
                # return True
                # go to look at playlist and mood history
                # pass  # for now
                return False
            elif user_answer == '2':
                return False
        except ValueError:
            Messages.end_menu_choices_error_msg()
            return User.end_menu_choices()

    def logout(self):
        if not User.end_menu_choices():
            self.username = None
            self.password = None
            self.email = None
            self.logged_in = False
            self.playlist = None
            self.mood_score = None
            self.entry_done = False
            self.date = None
            Messages.quit_msg()
