from sentiment_analysis import mood_analysis
from spotify_connect import *
from track_features import *
from create_playlist import create_playlist, select_mood_tracks
from datetime import date
from login_user import User
from Messages.messages import Messages

# authenticate spotify and get user and date details
sp = authenticate_spotify()
user = get_user_id(sp)
today = date.today()
name = today.strftime("%d/%m/%Y")

# Initialise User object called current_user, the date is today
current_user = User()
current_user.date = today

# current_user either registers or logs in or quits
if not current_user.has_account():
    Messages.register_msg()
    current_user.register()
else:
    current_user.login()

######## check if entry has already been made today by current user
######## give end menu: look at history, logout

# input the journal entry and determine mood
while True:
    try:
        entry = input('How are you feeling today?\n')
        mood = mood_analysis(entry)
        # set user mood attribute
        current_user.mood_score = mood
        print('Please wait, generating your playlist!')
    except Exception as exc:
        print(exc)
    else:
        break

# get the playlist info -> song info from playlist -> audio features from songs
playlist_ids = get_playlist_ids(sp)
list_tracks = get_playlist_tracks(playlist_ids, sp)
track_features = get_track_features(list_tracks, sp)


# get the track lists based on an algo and creates a spotify playlist
track_list = select_mood_tracks(mood, track_features)
new_playlist_id = create_playlist(sp, user, name, track_list[:20])
# set user playlist attribute
current_user.playlist = "https://open.spotify.com/playlist/{}".format(new_playlist_id)


# link to the new playlist
print('Play your new playlist at https://open.spotify.com/playlist/{}'.format(new_playlist_id))

####### give end menu: look at history, logout


# to check user attributes:
# print('\nThese are the current user attributes:\n')
# print(f'mood_score:{current_user.mood_score}')
# print(f"playlist link: {current_user.playlist}")
# print(f"logged in?: {current_user.logged_in}")
# print(f"username: {current_user.username}")
# print(f"email: {current_user.email}")
# print(f"pword: {current_user.password}")