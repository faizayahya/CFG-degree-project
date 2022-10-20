import mysql.connector
from db_files.db_config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


class Database:

    @staticmethod
    def connect_to_db():
        conx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database="SpotifyAppDB"
        )
        return conx


class InAccountsTable:
    @staticmethod
    def username_in_db_check(username):  # checks if username is already in the database, returns true if in db
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""SELECT username FROM accounts WHERE username = '{username}'"""
            my_cursor.execute(query)

        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        else:
            result = my_cursor.fetchall()
        try:
            if result[0][0] == username:
                return True
        except IndexError:
            return False
        finally:
            if db_conx:
                db_conx.close()

    @staticmethod
    def insert_new_user_to_db(username, password, email):
        if not InAccountsTable.username_in_db_check(username):
            try:
                db_conx = Database.connect_to_db()
                my_cursor = db_conx.cursor()

                query = (f"""INSERT INTO accounts (username, password, email)
                                    VALUES ('{username}', '{password}', '{email}');""")
                my_cursor.execute(query)
                db_conx.commit()

            except Exception:
                raise DbConnectionError("Failed to read data from DB")

            finally:
                if db_conx:
                    db_conx.close()

        else:
            print('Looks like you already have an account with us!')

    @staticmethod
    def authenticate_login_in_db(username, password):

        class PasswordError(Exception):
            pass

        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""SELECT username, password FROM accounts WHERE username = '{username}'"""
            my_cursor.execute(query)

        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        else:
            result = my_cursor.fetchall()
            if result[0][0] == username and result[0][1] == password:
                print('Successful Login')
                return True
            else:
                raise PasswordError
        finally:
            if db_conx:
                db_conx.close()

    @staticmethod
    def get_all_user_account_details():
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            my_cursor.execute("""SELECT * FROM accounts""")

            for i in my_cursor:
                print(i)

            my_cursor.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        finally:
            if db_conx:
                db_conx.close()


class InPlaylistsTable:
    @staticmethod
    def insert_playlist_to_db(username, playlist, mood_score, date):
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""INSERT INTO playlists (username, playlist_link, mood_score)
            VALUES {username}, {playlist}, {mood_score}, {date}"""

            my_cursor.execute(query)
            db_conx.commit()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_conx:
                db_conx.close()

    @staticmethod
    def fetch_playlist_mood_data(username):  # get copy of user's whole playlist history/mood history
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""SELECT date, playlist_link, mood FROM playlists WHERE username = {username}"""

            my_cursor.execute(query)
            result = my_cursor.fetchall()
            return result

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_conx:
                db_conx.close()

    @staticmethod
    def entry_done_today(date):  # returns true if an entry has been made, false if no entry
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""SELECT username FROM playlist WHERE date = '{date}'"""
            my_cursor.execute(query)
            result = my_cursor.fetchall()

            if result[0][0] == IndexError:  # if there is no result that means no entry made by user
                return False
            else:
                return True
        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        finally:
            if db_conx:
                db_conx.close()


class InTracksTable:
    @staticmethod
    def insert_song_data_to_db(song_name, song_uri, danceability, energy, valence):
        try:
            db_conx = Database.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"""INSERT INTO tracks (song_name, song_uri, danceability, energy, valence) 
            VALUES {song_name}, {song_uri}, {danceability}, {energy}, {valence}"""

            my_cursor.execute(query)
            db_conx.commit()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_conx:
                db_conx.close()
