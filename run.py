from sentiment_analysis import mood_analysis
from spotify_connect import *
from create_playlist import create_playlist, select_mood_tracks
from datetime import date

# authenticate spotify and get user and date details
sp = authenticate_spotify()
user = get_user_id(sp)
today = date.today()
name = today.strftime("%d/%m/%Y")

# get the playlist info -> song info from playlist -> audio features froms songs
playlist_ids = get_playlist_ids(sp)
song_ids, song_names, song_uris = get_playlist_tracks(playlist_ids, sp)
track_features = get_track_features(song_ids, song_names, song_uris, sp)

# input the journal entry and determine mood
entry = input('How are you feeling today?\n')
mood = mood_analysis(entry)

# get the track lists based on an algo and creates a spotify playlist
track_list = select_mood_tracks(mood, track_features)
new_playlist_id = create_playlist(sp, user, name, track_list[:20])

# link to the new playlist
print('Play your new playlist at https://open.spotify.com/playlist/{}'.format(new_playlist_id))

