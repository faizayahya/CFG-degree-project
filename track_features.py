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

# Something in the Water spotify:track:5z7wmSmPWHgTFz5iOKHhAz 0.573 0.739 0.591
# NIGHTS LIKE THESE spotify:track:33vZRjxJScapmRShRJq8I0 0.458 0.667 0.593
# Angel Baby spotify:track:2m6Ko3CY1qXNNja8AlugNc 0.338 0.559 0.559
# Colours Of You spotify:track:7hjPM7rlZo3netjXWOZqcT 0.251 0.482 0.542
# As It Was spotify:track:4LRPiXqCikLlN15c3yImP7 0.662 0.52 0.731
# Until I Found You spotify:track:0T5iIrXA4p5GsubkhuBIKV 0.227 0.539 0.508
# Glimpse of Us spotify:track:6xGruZOHLs39ZbVccQTuPZ 0.268 0.44 0.317
# That's Hilarious spotify:track:0wPKDeY4fZXT6k9bzV0kx0 0.546 0.713 0.442
# Cardboard Box spotify:track:2rf9i0Enr8cw1JRME8Rsvq 0.696 0.579 0.714
# you were there for me spotify:track:0C3shWEOObGT5IxApC7Mkg 0.409 0.571 0.845
# Ptolemaea spotify:track:29LsI5izZL8txZEJhegSBs 0.0349 0.281 0.374
# DOORWAY spotify:track:0GmGw3aqX1OLQdb88ECoe4 0.256 0.669 0.518
# No Love spotify:track:5fDj1YVNR04RtQNP4iYapO 0.608 0.547 0.884
# Aorta spotify:track:0UxLfXmjXU5qoRFL25n5lA 0.552 0.602 0.84
# Churpa Champurrado spotify:track:2nqZgkJdd2rfViWzGHR6aw 0.14 0.542 0.177
# You Never Came spotify:track:20rFw2Y26pbwK2qZV0nCKc 0.0317 0.118 0.182
# Saferoom spotify:track:1NO3x4XZW73pCXxLCPSNsI 0.0586 0.234 0.00474
# The Culling spotify:track:0aFXE1GU6jYnz8MkKyArZw 0.0361 0.263 0.34
# Burn It Down spotify:track:6pQhrodtxxhlXf9nUg6D6R 0.0794 0.818 0.316
# Lacrymaria Olor spotify:track:2VC3elGOA4t4khPnwyzWAx 0.141 0.48 0.444
# Another Guy - Acoustic spotify:track:7rWkd70fyKUGw00s6BBSGz 0.621 0.519 0.294
# Love Again spotify:track:6ZwNOYjJ06J77YF1ggXtaT 0.353 0.596 0.458
# Real Thing (feat. Tori Kelly) spotify:track:4Nk5iJrw4u7vJ6nGXosuxk 0.256 0.615 0.322
# Indonesian Fantasies spotify:track:3NktF1rRdORH8FH3p8wKp3 0.529 0.789 0.521
# our time spotify:track:6WBacWkfkwZxteVJ7MMBLZ 0.443 0.613 0.345
# Stop By spotify:track:2f4PvtF6upC4UWRE9yrF6v 0.43 0.765 0.6
# Khayaal spotify:track:4Yf5yQGD3pMKhhQJn85kpR 0.536 0.569 0.514
# Out Loud (feat. Kehlani) spotify:track:0P11qKeHWhUy0rDPeY8dyB 0.527 0.565 0.364
# Pressure spotify:track:4DixBDzCcjzWHICnRw4FGy 0.513 0.686 0.592
# Bittersweet Goodbyes spotify:track:1otiDJ357ZDfyaJpK4IvNQ 0.755 0.578 0.699
# SAD GIRLZ LUV MONEY Remix (feat. Kali Uchis and Moliy) spotify:track:09gysnJpfQ3ublBmJDfcEC 0.319 0.87 0.523
# dj spotify:track:3FkE7rIbfrkD5JluAGZtlt 0.244 0.555 0.614
# Cherries spotify:track:13z7RLPmgupzRwQY9NiTZU 0.772 0.795 0.693
# F.U.C.K. spotify:track:0iDuW211AjTsYDPsLxyqX4 0.464 0.761 0.397
# Speed Of Plight spotify:track:1t2YGrS7RAznI7zFR0aIIP 0.113 0.591 0.848
# G.O.Y.D. spotify:track:4jueyRHAHwDovQi3Nlce8v 0.587 0.667 0.623
# International Baby spotify:track:3jHqVzg1x0hBXlC6oRS6J2 0.356 0.828 0.793
# Sneaky spotify:track:6XkG4MmrybBwPUm2d4wD0c 0.587 0.861 0.449
# All My Girls Like To Fight spotify:track:6rCuplMDiFQVSca77OQocz 0.531 0.853 0.698
# Time Is Precious spotify:track:6hdFvWuFjmoxJjSeEjiJpg 0.0389 0.176 0.255
# on & on spotify:track:2fmtrXfvbN8xkHwE0zgTTc 0.819 0.609 0.765
# Evergreen (You Didn’t Deserve Me At All) spotify:track:2TktkzfozZifbQhXjT6I33 0.31 0.697 0.336
# October Passed Me By spotify:track:0AjcdGri5vhJsmZnduCEqd 0.202 0.445 0.367
# the perfect pair spotify:track:41P6Tnd8KIHqON0QIydx6a 0.6 0.634 0.663
# frog spotify:track:0nSw4I1cTMMBZBIk9ChgBn 0.563 0.611 0.461
# messy in heaven spotify:track:5RobAV5ROH5KARimi7n3cO 0.433 0.62 0.837
# Rips in Jeans spotify:track:7K0ga2R3IgiwDOZlk9SC9n 0.501 0.864 0.676
# Play Pretend spotify:track:0rpXpKiDSJ5QiAuo3JVky7 0.527 0.64 0.486
# Picture in my mind spotify:track:0z3YYobsavHguLTgqg5GC1 0.772 0.73 0.645
# say it spotify:track:1qYSKTn4Peb38J5828xUmF 0.501 0.644 0.584
# Delilah (pull me out of this) spotify:track:0Ftrkz2waaHcjKb4qYvLmz 0.586 0.685 0.827
# Water spotify:track:09cgbbadzZSKFd1hGN23p5 0.363 0.528 0.822
# Baianá spotify:track:7B0gxo0jQCy5Lk93RIODAC 0.411 0.531 0.89
# KILL DEM spotify:track:5CE0k1VmTXgCtaa5L288LP 0.291 0.788 0.873
# Problems spotify:track:1UERuR9hjz9GM609JIjtGx 0.534 0.703 0.873
# Defender spotify:track:4x9l3fDzgvzg9t7Csbufrn 0.482 0.711 0.769
# B.O.T.A. (Baddest Of Them All) spotify:track:45bfH0GZvUyujIBiKRhXso 0.749 0.756 0.962
# say it spotify:track:1qYSKTn4Peb38J5828xUmF 0.501 0.644 0.584
# Hungry (For Love) spotify:track:4Uz7te06snSlkmcIwwAvkw 0.49 0.605 0.973
# Shimmer spotify:track:6NzCy1aUFe3VOWRdnbmQN1 0.504 0.74 0.615
# Say Something spotify:track:6uF67kzG2wKwjt2LCAAy87 0.341 0.419 0.608
# Moves spotify:track:07DuoTCTocHk7y3d8MImks 0.628 0.753 0.765
# Summer In The Ends spotify:track:3ttIBQv2qjIWXbHeoCnoVm 0.39 0.795 0.651
# Song for My Mother spotify:track:53g6d5JlFL9HE6HXsIW5c1 0.416 0.64 0.598
# El Ritmo spotify:track:3pU6YE2xBTeyGt7d2v0mi2 0.551 0.745 0.806
# Rainbow Road spotify:track:2R9lqoximtsPHmnuvj3ptd 0.695 0.852 0.433
# Cumulus spotify:track:5uFYKPsV8x6D2swS6IXcWC 0.551 0.52 0.475
# Back in Tha Game spotify:track:7fJpSXw0yBa47OPDw5rdSP 0.64 0.588 0.744
# You Can't Steal My Joy spotify:track:1OlXIlGPGhoXI8f0Kj778C 0.91 0.57 0.861
# Un Caïd - Hello Skinny Remix spotify:track:2IKXhc8PLFJVogUslCFpeH 0.211 0.677 0.885
# Let’s Go Home Together - Stripped spotify:track:2cptaUFdsU60tdh7zRglai 0.331 0.649 0.441
# Remember - Acoustic spotify:track:5aXfGM7WVcqyAvqnL7k0y3 0.509 0.62 0.379
# Bad Habits - Acoustic Version spotify:track:0IkK4SEryuCtbQjm5LRLMZ 0.362 0.807 0.237
# Our Song - Acoustic spotify:track:6AJGPFFuC8qTWD5SP50RNh 0.539 0.546 0.475
# Paradise - Guitar Acoustic spotify:track:6GlMK7hhbyC0mlC3x5r3IY 0.589 0.644 0.514
# Starstruck - Acoustic spotify:track:4bEu5QXTW6yqkEdLmwmpmB 0.478 0.69 0.444
# What Other People Say - Stripped Version spotify:track:38AzxWkkEWzCE56drrO6Vx 0.25 0.692 0.335
# You - Acoustic spotify:track:7IoyTDxOTWYkHx1f3oWhtt 0.267 0.405 0.528
# Black Hole - Acoustic Version spotify:track:1cpVLszZnKUHUjsJDTEi3D 0.227 0.824 0.3
# Is It Just Me? (feat. JP Cooper) (Acoustic) spotify:track:2KJdJ2GPBhWBr0vugLCrOz 0.403 0.574 0.345
# Drunken Clouds spotify:track:0JF3Ju6TpQjwnnH10B9kpu 0.0974 0.566 0.666
# I've Been Thinking A Lot Lately spotify:track:2ELhlJLWntX7IVZdmLUDiY 0.136 0.582 0.729
# The Look of Accessibility spotify:track:3mg8dRdGN5jg0KqWqKh9pj 0.264 0.801 0.549
# Dreaming of Sunflowers spotify:track:1EWTNKqsTh5E4fndYQlor6 0.663 0.77 0.654
# An Exhale spotify:track:1Cdi1HIK4bJD3F8HGKZDQQ 0.258 0.801 0.846
# Inlove2 - Edit spotify:track:5E2gMJ9KAbaVAscQ20N7Xk 0.0954 0.591 0.877
# Girde Maye/Astere spotify:track:7om1pOBGjSXTl2KxzdKOTo 0.529 0.526 0.886
# Olga spotify:track:1jCOMWObV0nWG0qqjcPKwi 0.0344 0.0814 0.266
# Efflorescence spotify:track:2ZIv64u8EDj0BjecR7IaB2 0.546 0.517 0.697
# Bassline Interferometry spotify:track:2uouZv9rjjl4FkSs5jSkhc 0.0953 0.648 0.625
# Big Fat Liar spotify:track:0zMulZKhUroYHauRqdp9j3 0.499 0.738 0.536
# Distraction spotify:track:2WPwDmI4pmK5S9wBrKDMKo 0.539 0.67 0.477
# Love Will Get You There spotify:track:0UgCI5TiOQthbrEVSqHC9j 0.527 0.504 0.897
# Come Ouu (feat. Jrilla) spotify:track:5AZfN1S0gAbaMtgrOFoxsD 0.61 0.798 0.571
# Believe In Love spotify:track:56GN8iXX2Hvx2Duorz0Xri 0.417 0.592 0.779
# Spotlight Television spotify:track:5o5CADtcyCZFR2COk8EJ2g 0.278 0.542 0.574
# ILY2 spotify:track:7tgteKiRkLq30c9qG4mWQr 0.489 0.48 0.725
# Never Mind spotify:track:7AsR6M00PcFOQP5Nh9xgTN 0.724 0.497 0.896
# Love Like This spotify:track:0eVoQFUtCL9Bpwky003Ows 0.604 0.664 0.733
# This Is What They Meant spotify:track:0tZHm9L4ssbjBoJ2N5vOiK 0.82 0.68 0.79
# Footloose - From "Footloose" Soundtrack spotify:track:4YR6Dextuoc3I8nJ0XgzKI 0.911 0.582 0.564
