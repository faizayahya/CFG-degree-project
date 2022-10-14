import spotipy
from spotipy.oauth2 import SpotifyOAuth
from settings import *


def authenticate_spotify():
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

    scope = "user-library-read user-top-read user-follow-read playlist-modify-public streaming"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


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


def get_playlist_tracks(playlist_ids, sp):
    list_song_ids = []
    list_song_names = []
    list_song_uri = []
    for playlist in playlist_ids:
        tracks = sp.playlist_items(playlist, fields=None, limit=10, offset=0, market='GB',
                                   additional_types=('track', 'episode'))

        for track in tracks['items']:
            song = track['track']
            if song is not None:
                list_song_ids.append(song['id'])
                list_song_names.append(song['name'])
                list_song_uri.append(song['uri'])

    return list_song_ids, list_song_names, list_song_uri


def get_track_features(song_ids_list, song_names_list, song_uris_list, sp):
    list_song_audio_features = []
    features_list = sp.audio_features(tracks=song_ids_list)
    for features in features_list:
        song_audio_features = {'valence': features['valence'],
                               'danceability': features['danceability'],
                               'energy': features['energy']}
        list_song_audio_features.append(song_audio_features)

    count = 0
    for item in list_song_audio_features:
        item['number'] = count
        item['song_name'] = song_names_list[count]
        item['song_id'] = song_ids_list[count]
        item['song_uri'] = song_uris_list[count]
        count += 1

    return list_song_audio_features


