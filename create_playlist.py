
def select_mood_tracks(mood_score, tracks):
    selected_tracks = []
    for track in tracks:
        if mood_score > 0.05:
            if track['danceability'] > 0.5 and track['valence'] > 0.5:
                selected_tracks.append(track)
        elif mood_score < -0.05:
            if track['danceability'] < 0.5 and track['valence'] < 0.5:
                selected_tracks.append(track)
        else:
            if -0.05 < mood_score < 0.05:
                if 0.3 < track['danceability'] < 0.6 and 0.3 < track['valence'] < 0.6:
                    selected_tracks.append(track)
    return selected_tracks


def create_playlist(sp, username, playlist_name, track_list):
    track_list_ids = []
    for track in track_list:
        track_list_ids.append(track['song_uri'])

    mood_playlist = sp.user_playlist_create(username, playlist_name, public=True, collaborative=False, description='')
    mood_playlist_id = mood_playlist["id"]
    sp.playlist_add_items(mood_playlist_id, track_list_ids, position=None)
    return mood_playlist_id
