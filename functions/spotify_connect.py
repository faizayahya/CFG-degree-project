import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ..settings import *
import os


# TO DO: put as method in a User Class
def authenticate_spotify():
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

    scope = "user-library-read user-top-read user-follow-read playlist-modify-public streaming"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


# TO DO: put as method in a User Class
def get_user_id(sp):
    user_id = sp.me()['id']
    return user_id


def get_playlist_ids(sp):
    res = sp.featured_playlists(locale='en_GB', country='GB', timestamp=None, limit=10, offset=0)
    playlists = res['playlists']['items']
    playlist_ids = []
    for playlist in playlists:
        playlist_id = playlist['id']
        playlist_ids.append(playlist_id)

    return playlist_ids


# Playlist class: playlist id, list of track objects

