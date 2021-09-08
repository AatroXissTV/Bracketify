# Entry Point
# Created Sep 03, 2021 at 14:24 CEST
# Last updated Sep 09, 2021 at 16:07 CEST

# Standard imports

# Third-party imports

# Local imports
from controllers.game_controller import GameController

# Other imports


def main():
    """Entry Point
    """

    launch = GameController("Bracketify")
    launch.start()


main()
