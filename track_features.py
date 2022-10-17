class Track:

    def __init__(self):
        self.name = ''
        # self.id = ''
        self.uri = ''
        # self.playlist = ''
        self.danceability = 0
        self.energy = 0
        self.valence = 0

    def get_track_name(self, song):
        self.name = song['name']

    # def get_track_id(self, song):
    #     self.id = song['id']

    def get_track_uri(self, song):
        self.uri = song['uri']

    def get_playlist_id(self, playlist):
        self.playlist = playlist

    def get_danceability(self, features):
        self.danceability = features['danceability']

    def get_energy(self, features):
        self.energy = features['energy']

    def get_valence(self, features):
        self.valence = features['valence']


def get_playlist_tracks(playlist_ids, sp):
    list_tracks = []
    for playlist in playlist_ids:
        tracks = sp.playlist_items(playlist, fields=None, limit=10, offset=0, market='GB',
                                   additional_types=('track', 'episode'))
        for track in tracks['items']:
            song = track['track']
            if song is not None:
                obj = Track()
                obj.get_track_name(song)
                # obj.get_track_id(song)
                obj.get_track_uri(song)
                list_tracks.append(obj)
    return list_tracks


def get_track_features(track_object_list, sp):
    for track_object in track_object_list:
        features_list = sp.audio_features(tracks=[track_object.uri])

        for features in features_list:
            track_object.get_danceability(features)
            track_object.get_energy(features)
            track_object.get_valence(features)

    return track_object_list
