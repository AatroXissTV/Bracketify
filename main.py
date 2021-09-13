# Entry Point
# Created Sep 03, 2021 at 14:24 CEST
# Last updated Sep 13, 2021 at 15:11 CEST

# Standard imports

# Third-party imports

# Local imports
from controllers.game_controller import GameController

# Other imports


def main():
    """Entry Point

    Initialize GameController and call start().
    Uses app name in parameter
    """

    launch = GameController("Bracketify")
    launch.start()


main()
