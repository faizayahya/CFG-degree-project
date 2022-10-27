import random
from db_files.db_utils import InTracksTable

def select_mood_tracks(mood_score, tracks):
    selected_tracks = []
    for track in tracks:
        if mood_score > 0.05:
            if track.danceability > 0.5 and track.valence > 0.5:
                selected_tracks.append(track)
        elif mood_score < -0.05:
            if track.danceability < 0.5 and track.valence < 0.5:
                selected_tracks.append(track)
        else:
            if -0.05 < mood_score < 0.05:
                if 0.3 < track.danceability < 0.6 and 0.3 < track.valence < 0.6:
                    selected_tracks.append(track)

    return selected_tracks

def get_full_tracklist(track_objects, mood_score):
    track_list_uris = []
    for track in track_objects:
        track_list_uris.append(track.uri)

    db_tracks = InTracksTable.get_mood_tracks(mood_score=mood_score)
    track_list_uris.append(db_tracks)

    random.shuffle(track_list_uris)

    return track_list_uris


def create_playlist(sp, username, playlist_name, track_list_uris):

    mood_playlist = sp.user_playlist_create(username, playlist_name, public=True, collaborative=False, description='')
    mood_playlist_id = mood_playlist["id"]
    sp.playlist_add_items(mood_playlist_id, track_list_uris, position=None)
    return mood_playlist_id

