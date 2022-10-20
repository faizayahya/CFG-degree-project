import mysql.connector
from db_config import HOST, USER, PASSWORD

# input your hostname, password, and username for your mysql below:

# HOST = ""
# USER = ""
# PASSWORD = ""

# make sure mysql-connector-python is installed

# once installed then run this file

create_accounts_table_query = """
CREATE TABLE IF NOT EXISTS accounts (
username VARCHAR(30) NOT NULL PRIMARY KEY,
password VARCHAR(30) NOT NULL,
email VARCHAR(100) NOT NULL
);
"""

create_playlists_table_query = """
CREATE TABLE IF NOT EXISTS playlists (
username VARCHAR(30) NOT NULL PRIMARY KEY,
playlist_link VARCHAR(200),
mood_score FLOAT NOT NULL,
date DATE NOT NULL
);
"""

create_tracks_table_query = """
CREATE TABLE IF NOT EXISTS tracks (
song_name VARCHAR(100) NOT NULL,
song_id VARCHAR(100) NOT NULL,
song_uri VARCHAR(100) NOT NULL,
energy FLOAT NOT NULL,
valence FLOAT NOT NULL,
danceability FLOAT NOT NULL
);
"""

insert_dummy_data_to_accounts = """
INSERT INTO accounts (username, password, email)
VALUES
('aaliya', 'aaliya123', 'aaliya@email.com'),
('barbie', 'barbieGIRL', 'bbgirl@email.com'),
('donald', 'ducky', 'd.duck@email.com'),
('faiza', 'fay123', 'faiza@email.com'),
('humi', 'humi123', 'humi@email.com'),
('ken', 'barbie4life', 'kendoll@email.com'),
('link', 'hyaah', 'im_not_zelda@email.com'),
('makayla', 'mak123', 'makayla@email.com'),
('mickey', 'misterMOUSE', 'the_mouse@email.com'),
('orange', 'tropicalFRUIT', 'oraoraora@email.com'),
('priyanka', 'priya123', 'priyanka@email.com'),
('zorro', 'zor123', 'zor@email.com')
"""

# zorro is my cat

cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
            # auth_plugin='mysql_native_password',
            # database="SpotifyAppDB"
        )

cur = cnx.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS SpotifyAppDB;")
cur.execute("USE SpotifyAppDB;")
cur.execute(create_accounts_table_query)
cur.execute(create_playlists_table_query)
cur.execute(create_tracks_table_query)
cur.execute(insert_dummy_data_to_accounts)

cnx.commit()
cnx.close()

#########################################
#                                       #
#   YOU NOW HAVE THE DATABASE SET UP!   #
#                                       #
#########################################



