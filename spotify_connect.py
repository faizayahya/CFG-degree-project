import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from settings import *

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = "user-library-read user-top-read user-follow-read playlist-modify-public streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

res = sp.featured_playlists(locale='en_GB', country='GB', timestamp=None, limit=20, offset=0)
playlists = res['playlists']['items']
playlist = playlists[0]
playlist_id = playlist['id']

tracks = sp.playlist_items(playlist_id, fields=None, limit=10, offset=0, market='GB',
                           additional_types=('track', 'episode'))

for track in tracks['items']:
    song = track['track']
    song_id = song['id']

    features = sp.audio_features(tracks=[song_id])
    print(song['name'])
    print('danceability: {}'.format(features[0]['danceability']))
    print('valence: {}'.format(features[0]['valence']))
    print('energy: {}'.format(features[0]['energy']))
