from prettytable import PrettyTable
import pyfiglet


def welcome():

    title = pyfiglet.figlet_format("Daily  Records", font='Shimrod', justify='center')

    tagline = "transform your journal entries into spotify playlists".title()

    print(title)
    print(f"{tagline:^80}\n")


def create_history_table(history):
    table = PrettyTable(['DATE', 'MOOD SCORE', 'LINK'])
    table.padding_width = 3
    table.float_format = ".4"

    for row in history:
        table.add_row(row)

    return table
