# views/cli_views.py
# created 22/09/2021 @ 22:09 CEST
# last updated 28/09/2021 @ 10:26 CEST

""" views/cli_views.py

To do:
    * Add tasks
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports
import os
from time import sleep

# third-party imports
from pyfiglet import Figlet

# local imports

# other


class Cli():
    """this class represents the command line interface for Bracketify
    """

    def __init__(self, app_title):
        """Constructor

        - Args:
            app_title -> str
        """

        self.figlet_font = "doom"
        self.app_title = app_title
        self.title_font = Figlet(font=self.figlet_font)

    """Summary of methods and quick explanation

    - Methods:
        display_title(self):
            display app_title with Figlet

    - ClassMethods:
        cli_entry(title):
            clear screen then calls display_title

        cli_delay(cls, delay=3, second_delay=1):
            delay new screen

        cli_delay_no_interaction(cls):
            Delay new screen but doesn't return to the user
            a message that says software is interacting with
            the database.

        cli_clear(cls):
            clear screen

    """

    def display_title(self) -> str:
        print("{}\n".format(self.title_font.renderText(self.app_title)))

    @staticmethod
    def cli_entry(title):
        view_cli = Cli(app_title=title)
        view_cli.cli_clear()
        view_cli.display_title()

    @classmethod
    def cli_delay(cls):
        print("Please wait, I'm interacting with the database")
        sleep(2)
        print("It's ok, I saved your changes")
        sleep(1)

    @classmethod
    def cli_delay_no_interaction(cls):
        print("...")
        sleep(2)
        print("Done")
        sleep(1)

    @classmethod
    def cli_clear(cls):
        os.system('cls')
