class Messages:
    @staticmethod
    def register_msg():
        print('Register with us!\n')

    @staticmethod
    def has_account_error_msg():
        print('Enter 1 for Yes or 2 for no. Please try again')

    @staticmethod
    def try_email_again_msg():
        print('That does not seem to be an email. Please enter your email in this format:\n'
              'email@email.com')

    @staticmethod
    def set_uname_pword_msg():
        print('Set a username and password and write your email address.\n')

    @staticmethod
    def quit_msg():
        print('Thank you for using our app')

    @staticmethod
    def duplicate_username_msg():
        print('\nSorry! This username is already taken. You may already have an account with us.\n')

    @staticmethod
    def new_account_success_msg():
        print('New account successfully created')

    @staticmethod
    def entry_already_made_msg():
        print("\nSeems like you've already generated a playlist today!\n")
