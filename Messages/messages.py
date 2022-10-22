class Messages:
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
        print('\nSet a username and password and write your email address.\n')

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
        print("Enter 1 to look at history or 2 to logout")
