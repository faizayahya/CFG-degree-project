class Messages:
    @staticmethod
    def invalid_username_msg():
        print('\nThis is an invalid username. Please enter a username between 3 and 10 characters. '
              'Please do not user any special characters\n')

    @staticmethod
    def invalid_password_msg():
        print('\nThis is an invalid password. Please enter a password longer than 4 characters.\n')

    @staticmethod
    def register_msg():
        print('\nRegister with us!\n')

    @staticmethod
    def has_account_error_msg():
        print('\nEnter 1 for Yes, 2 for No, or 3 to Quit. Please try again\n')

    @staticmethod
    def try_email_again_msg():
        print('\nThat does not seem to be an email. Please enter your email in this format:\n'
              'email@email.com\n')

    @staticmethod
    def set_uname_pword_msg():
        print('Set a username and password and write your email address.\n')

    @staticmethod
    def too_many_attempts():
        print('\nYou have reached the number of attempts to input your password\n')

    @staticmethod
    def incorrect_password():
        print("\nIncorrect password, please try logging in again\n")

    @staticmethod
    def quit_msg():
        print('\nThank you for using our app\n')

    @staticmethod
    def duplicate_username_msg():
        print('\nSorry! This username is already taken. You may already have an account with us.\n')

    @staticmethod
    def new_account_success_msg():
        print('\nNew account successfully created\n')

    @staticmethod
    def entry_already_made_msg():
        print("\nSeems like you've already generated a playlist today!\n")

    @staticmethod
    def end_menu_choices_error_msg():
        print("\nEnter 1 to look at history or 2 to logout\n")

    @staticmethod
    def something_went_wrong():
        print('\nSomething went wrong, please try again\n')
