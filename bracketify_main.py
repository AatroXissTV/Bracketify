# bracketify_main.py
# created 22/09/2021 @ 22:50 CEST
# last updated 22/09/2021 @ 22:50 CEST

""" bracketify_main.py

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

# third-party imports

# local imports
from controllers.game_controllers import GameController

# other


def main():
    """Is the entry point for the application
    """

    launch_app = GameController("Bracketify")
    launch_app.start_app()


main()
