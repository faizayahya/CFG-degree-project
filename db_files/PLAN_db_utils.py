import mysql.connector
from db_config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass


class DatabaseConnect:
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
            db_conx = DatabaseConnect.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"SELECT username FROM accounts WHERE username = '{username}'"
            my_cursor.execute(query)

        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        else:
            result = my_cursor.fetchall()
        try:
            if result[0][0] == username:
                # print('true')
                return True
        except IndexError:
            return False
        finally:
            if db_conx:
                db_conx.close()

    # InAccountsTable.username_in_db_check('barbie')

    @staticmethod
    def insert_new_user_to_db(username, password, email):
        if not InAccountsTable.username_in_db_check(username):
            try:
                db_conx = DatabaseConnect.connect_to_db()
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
                print('New account successfully created')
        else:
            print('Looks like you already have an account with us!')

    # InAccountsTable.insert_new_user_to_db("link", "hyaah", "im_not_zelda@email.com")

    @staticmethod
    def authenticate_login_in_db(username, password):

        class PasswordError(Exception):
            pass

        try:
            db_conx = DatabaseConnect.connect_to_db()
            my_cursor = db_conx.cursor()

            query = f"SELECT username, password FROM accounts WHERE username = '{username}'"
            my_cursor.execute(query)

        except Exception:
            raise DbConnectionError("Failed to read data from DB")
        else:
            result = my_cursor.fetchall()
            if result[0][0] == username and result[0][1] == password:
                print('you may proceed')
                return True
            else:
                raise PasswordError
        finally:
            if db_conx:
                db_conx.close()

    # InAccountsTable.authenticate_login_in_db("link", "hyaah")

    @staticmethod
    def get_user_details():
        try:
            db_conx = DatabaseConnect.connect_to_db()
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

# InAccountsTable.get_user_details()


# access into playlists table
# insert data into playlists
# same for tracks