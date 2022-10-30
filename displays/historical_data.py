from db_files.db_utils import *
from prettytable import PrettyTable


def create_table(history):
    table = PrettyTable(['DATE', 'MOOD SCORE', 'LINK'])
    for row in history:
        table.add_row(row)

    return table

#
user_history = (InPlaylistsTable.fetch_playlist_mood_data("humi"))  # --> list of tuples
#
print(create_table(user_history))
