from sentiment_analysis import mood_analysis
from spotify_connect import *
from track_features import *
from create_playlist import create_playlist, select_mood_tracks
from datetime import date

# authenticate spotify and get user and date details
sp = authenticate_spotify()
user = get_user_id(sp)
today = date.today()
name = today.strftime("%d/%m/%Y")

# input the journal entry and determine mood
while True:
    try:
        entry = input('How are you feeling today?\n')
        mood = mood_analysis(entry)
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

# link to the new playlist
print('Play your new playlist at https://open.spotify.com/playlist/{}'.format(new_playlist_id))

