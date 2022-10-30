from db_files.db_utils import *
from prettytable import PrettyTable
import pyfiglet


def create_history_table(history):
    table = PrettyTable(['DATE', 'MOOD SCORE', 'LINK'])
    table.padding_width = 3
    table.float_format = ".4"

    for row in history:
        table.add_row(row)

    return table


# user_history = (InPlaylistsTable.fetch_playlist_mood_data("ken"))  # --> list of tuples
# print(create_table(user_history))

# (datetime.date(2022, 10, 26), -0.569059, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 25), -0.07421, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 24), 0.2467, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 23), 0.8732, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 22), 0.03, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 21), -0.569059, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')
# (datetime.date(2022, 10, 20), 0.76321, 'https://open.spotify.com/playlist/4jCXaG1BZEhn50k44k0Ntu')

def welcome():

    title = pyfiglet.figlet_format("Daily  Records", font='Shimrod', justify='center')

    tagline = "transform your journal entries into spotify playlists".title()

    print(title)
    print(f"{tagline:^80}\n")
