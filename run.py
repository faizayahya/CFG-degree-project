from functions_tests.sentiment_analysis import *
from functions_tests.spotify_connect import *
from functions_tests.track_features import *
from functions_tests.create_playlist import create_playlist, select_mood_tracks
from functions_tests.login_user import User
from Displays.messages import *
from db_files.db_utils import InPlaylistsTable, InAccountsTable
from Displays.prints import create_history_table, welcome
from datetime import date


def main():
    welcome()
    # authenticate spotify and get user and date details
    sp = authenticate_spotify()
    user = get_user_id(sp)
    today = date.today()
    name = today.strftime("%d/%m/%Y")

    # Initialise User object called current_user, their date is today
    current_user = User()
    current_user.date = str(name)

    # check if user has account, if so login, if not then set up new account
    if current_user.has_account():
        current_user.login()
    else:
        register_msg()
        current_user.set_username()
        if InAccountsTable.username_in_db_check(current_user.username):
            duplicate_username_msg()
            if current_user.wants_to_login():
                current_user.login()
            else:
                exit()
        else:
            current_user.set_password()
            current_user.set_email()
            InAccountsTable.insert_new_user_to_db(current_user.username,
                                                  current_user.password,
                                                  current_user.email)
            new_account_success_msg()
            current_user.logged_in = True

    # check if entry has already been made today by current user
    if not current_user.entry_made():
        # input the journal entry and determine mood
        try:
            entry = input('\nHow are you feeling today?\n')
            mood = mood_analysis(entry)
            # set user mood attribute
            current_user.mood_score = mood
            print('\nPlease wait, generating your playlist!\n')
        except Exception as exc:
            print(exc)

        # get the playlist info -> song info from playlist -> audio features from songs
        playlist_ids = get_playlist_ids(sp)
        tracks = get_playlist_tracks(playlist_ids, sp)
        list_tracks = get_track_list(tracks)
        track_features = get_all_track_features(list_tracks, sp)

        # get the track lists based on an algo and creates a spotify playlist
        track_list = select_mood_tracks(mood, track_features)
        new_playlist_id = create_playlist(sp, user, name, track_list[:20])

        # set user playlist attribute
        current_user.playlist = "https://open.spotify.com/playlist/{}".format(new_playlist_id)

        # insert playlist data, mood, user in playlist table
        InPlaylistsTable.insert_playlist_to_db(current_user.username,
                                               current_user.playlist,
                                               current_user.mood_score,
                                               current_user.date)

        # link to the new playlist
        print('\nPlay your new playlist at https://open.spotify.com/playlist/{}\n\n'.format(new_playlist_id))

    else:
        entry_already_made_msg()

    if current_user.end_menu_choices():
        user_history = (InPlaylistsTable.fetch_playlist_mood_data(current_user.username))
        print()
        print(create_history_table(user_history))

    current_user.logout()


if __name__ == "__main__":
    main()

    # print('\nThese are the current user attributes:\n')
    # print(f'mood_score:{current_user.mood_score}')
    # print(f"playlist link: {current_user.playlist}")
    # print(f"logged in?: {current_user.logged_in}")
    # print(f"username: {current_user.username}")
    # # print(f"email: {current_user.email}")
    # # print(f"pword: {current_user.password}")
    # print(f"date: {current_user.date}")
