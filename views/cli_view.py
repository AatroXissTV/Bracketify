# cli_view.py
# Created Aug 31, 2021 at 15:37 CEST
# Last updated Sep 13, 2021 at 15:25 CEST

# Standard imports
import os
from time import sleep

# Third-party imports
from pyfiglet import Figlet

# Local imports

# Other imports


class Cli():
    """Represents the Command line interface view
    """

    def __init__(self, app_title):
        """Constructor

        - Args :
            app_title -> str
                is the name of the app => Bracketify
        """

        self.figlet_font = "doom"
        self.app_title = app_title
        self.app_title_font = Figlet(font=self.figlet_font)

    """Methods used in CLi view class

    - Methods:
        display_title(self):
            Used to display app title/

    - StaticMethods:

        cli_entry(title):
            This method is used when a new menu/page is displayed.
            It uses previous functions to make it one.
            clear screen and then display title

        delay_new_screen():
            Used to delay the transition between 2 screens.

        clear_screen():
            Used to clear screen when navigating between menus.
    """

    def display_title(self) -> str:
        print("{}\n".format(self.app_title_font.renderText(self.app_title)))

    @staticmethod
    def cli_entry(title):
        view_cli = Cli(app_title=title)
        view_cli.clear_screen()
        view_cli.display_title()

    @staticmethod
    def cli_delay(delay=5, delay_end=1):
        print("Wait...")
        sleep(delay)
        print("Done.")
        sleep(delay_end)

    @staticmethod
    def clear_screen():
        os.system('cls')
