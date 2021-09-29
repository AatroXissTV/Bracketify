# controllers/game_controllers.py
# created 22/09/2021 @ 22:55 CEST
# last updated 28/09/2021 @ 11:56 CEST

""" controllers/game_controller.py

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
from views.cli_views import Cli
from views.main_views import MainMenu
from controllers.round_controllers import RoundController
from controllers.tournament_controllers import TournamentController
from controllers.player_controllers import PlayerController

# other


class GameController():
    """this class represents the game controller of Bracketify

    Manages main_menu & submenu logic
    """

    def __init__(self, app_title):
        """Constructor

        - Args:
            app_title -> str
        """

        self.app_title = app_title

    """Summary of methods and quick explanation

    - start_app(self):
        represents the main menu of the app

    - reports_submenu(title):
        used to manage reports submenu

    - order_submenu(title):
        used to manage order submenu.

    - return_to_main(title):
        used to ask if the user wants to return to main.
    """

    def start_app(self):
        title = self.app_title
        view_menu = MainMenu(app_title=title)

        while (view_menu != 'Quit'):
            Cli.cli_entry(title)
            print("I whalecome (welcome) you to Bracketify")
            print("You can now navigate through the menu")
            print("Don't hesitate to give a star on Github\n")
            main_menu = view_menu.main_menu()

            if (main_menu == "Add a new player"):
                PlayerController.add_a_new_player_menu(title)

            elif (main_menu == "Changes a player's rank"):
                PlayerController.modify_player_rank_menu(title)

            elif (main_menu == "Add a new tournament"):
                TournamentController.add_a_new_tournament_menu(title)

            elif (main_menu == "Launch a tournament"):
                TournamentController.launch_a_tournament(title)

            elif (main_menu == "View reports"):
                GameController.reports_submenu(title)

            elif (main_menu == "Quit"):
                Cli.cli_clear()
                exit()

    # Submenu -> Reports
    def reports_submenu(title):
        Cli.cli_entry(title)
        view_menu = MainMenu(app_title=title)
        print("Here you can see all reports about :")
        print("players, tournaments, matches and rounds\n")

        reports_submenu = view_menu.reports_submenu()

        if (reports_submenu == "players"):
            players_list = PlayerController.display_players(title)
            GameController.order_submenu(title, players_list)

        elif (reports_submenu == "tournaments"):
            TournamentController.display_tournaments(title)
            GameController.return_to_main(title)

        elif (reports_submenu == "players in a tournament"):
            players_list = TournamentController.display_p_in_t(title)
            GameController.order_submenu(title, players_list)

        elif (reports_submenu == "all rounds in a tournament"):
            RoundController.display_r_in_t(title)
            GameController.return_to_main(title)

        elif (reports_submenu == "all the matches of a tournament"):
            TournamentController.display_m_in_t(title)
            GameController.return_to_main(title)

        elif (reports_submenu == "return to main menu"):
            Cli.cli_clear()
            return_to_main = GameController(title)
            return_to_main.start_app()

    # Submenu -> Order players submenu
    def order_submenu(title, players_list):
        view_menu = MainMenu(app_title=title)
        order_submenu = view_menu.order_submenu()

        if (order_submenu == "by alphabetical order (a -> z)"):
            PlayerController.display_alphabetical_p_atoz(title, players_list)
            GameController.return_to_main(title)

        elif (order_submenu == "by alphabetical order (z -> a)"):
            PlayerController.display_alphabetical_p_ztoa(title, players_list)
            GameController.return_to_main(title)

        elif (order_submenu == "by rank order (1 -> x)"):
            PlayerController.display_rank_p_1tox(title, players_list)
            GameController.return_to_main(title)

        elif (order_submenu == "by rank order (x -> 1)"):
            PlayerController.display_rank_p_xto1(title, players_list)
            GameController.return_to_main(title)

        elif (order_submenu == "return to reports menu"):
            GameController.reports_submenu(title)

    def return_to_main(title):
        view_menu = MainMenu(app_title=title)
        return_submenu = view_menu.return_to_main()

        if (return_submenu == 'True'):
            Cli.cli_clear()
            GameController(title)
        else:
            pass
