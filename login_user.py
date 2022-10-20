import db_files.db_utils as db
from Menus.menus import Menus
from Messages.messages import Messages
import re


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
            do_you_have_account = input('')
            if do_you_have_account == "1" or do_you_have_account == 'yes' or do_you_have_account == 'Yes':
                return True
            elif do_you_have_account == "2" or do_you_have_account == 'no' or do_you_have_account == 'No':
                return False
            if do_you_have_account == "3" or do_you_have_account == "q" or do_you_have_account == "Quit":
                Messages.quit_msg()
                exit()
        except ValueError:
            Messages.has_account_error_msg()
            User.has_account()
        else:
            Messages.has_account_error_msg()
            User.has_account()

    def register(self):
        Messages.set_uname_pword_msg()
        self.username = input('Set a username:')

        account_exists = db.InAccountsTable.username_in_db_check(self.username)
        if account_exists:
            Messages.duplicate_username_msg()
            if self.wants_to_login():
                self.login()
            else:
                exit()

        else:
            self.password = input('Set a password:')
            email_entry = input('Please write your email address:')

            if User.email_is_valid(email_entry):
                self.logged_in = True
                self.email = email_entry
                db.InAccountsTable.insert_new_user_to_db(self.username, self.password, self.email)
                Messages.new_account_success_msg()

            else:
                Messages.try_email_again_msg()
                return self.register()

    @staticmethod
    def email_is_valid(email_entry):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email_entry):
            return False
        else:
            return True

    def wants_to_login(self):
        Menus.wants_to_login_menu()
        user_answer = input('')
        if user_answer == '1':
            return True
        elif user_answer == '2':
            self.register()
        elif user_answer == '3':
            Messages.quit_msg()
            return False
        else:
            print('Please enter 1 to Login, 2 to register with a different account, or 3 for Quit')
            return self.wants_to_login()

    def login(self):
        self.username = input('Please enter your username:')
        self.password = input('Please enter your password:')
        if db.InAccountsTable.authenticate_login_in_db(self.username, self.password):
            self.logged_in = True

    def entry_made(self):
        if db.InPlaylistsTable.entry_made_check_db(self.username, self.date):
            return True
        else:
            return False

    @staticmethod
    def end_menu_choices():
        Menus.end_menu()
        user_answer = input('')
        if user_answer == '1':
            # return True
            # go to look at playlist and mood history
            pass  # for now
        elif user_answer == '2':
            return False

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
