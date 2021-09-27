# controllers/game_controllers.py
# created 22/09/2021 @ 22:55 CEST
# last updated 22/09/2021 @ 22:55 CEST

""" controllers/game_controller.py

To do:
    * insert tasks
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.5.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports

# third-party imports

# local imports
from controllers.tournament_controllers import TournamentController
from models.player_models import Player
from views.cli_views import Cli
from views.main_views import MainMenu
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
    """

    def start_app(self):
        title = self.app_title
        view_menu = MainMenu(app_title=title)

        while (view_menu != 'Quit'):
            Cli.cli_entry(title)
            print("I whalecome you to Bracketify")
            print("You can now navigate through the menu")
            print("Don't hesitate to give a star on Github\n")
            main_menu = view_menu.main_menu()

            if (main_menu == "Add a new player"):
                Cli.cli_entry(title)
                PlayerController.add_a_new_player_menu(title)
                Cli.cli_delay()

            elif (main_menu == "Changes a player's rank"):
                Cli.cli_entry(title)
                PlayerController.modify_player_rank_menu(title)

            elif (main_menu == "Add a new tournament"):
                Cli.cli_entry(title)
                TournamentController.add_a_new_tournament_menu(title)

            elif (main_menu == "Launch a tournament"):
                Cli.cli_entry(title)
                TournamentController.launch_a_tournament(title)

            elif (main_menu == "View reports"):
                Cli.cli_entry(title)
                GameController.reports_submenu(title)
                Cli.cli_clear()

            elif (main_menu == "Quit"):
                Cli.cli_clear()
                exit()

    def reports_submenu(title):
        view_menu = MainMenu(app_title=title)
        reports_submenu = view_menu.reports_submenu()

        if (reports_submenu == "players"):
            Cli.cli_entry(title)
            players_docid_list = Player.load_players_docid_db()
            players_list = []
            for player_docid in players_docid_list:
                player = Player.get_player_w_docid(player_docid)
                players_list.append(player)
            GameController.order_submenu(title, players_list)

        elif (reports_submenu == "tournaments"):
            Cli.cli_entry(title)
            TournamentController.display_tournaments(None)
            GameController.return_to_main(title)
            Cli.cli_delay_no_interaction()

        elif (reports_submenu == "players in a tournament"):
            Cli.cli_entry(title)
            players_list = TournamentController.display_p_in_t(None, title)
            GameController.order_submenu(title, players_list)

        elif (reports_submenu == "all rounds in a tournament"):
            Cli.cli_entry(title)
            Cli.cli_delay()

        elif (reports_submenu == "all the matches of a tournament"):
            Cli.cli_entry(title)
            Cli.cli_delay()

        elif (reports_submenu == "return to main menu"):
            Cli.cli_clear()
            return_to_main = GameController(title)
            return_to_main.start_app()

    def order_submenu(title, players_list):
        view_menu = MainMenu(app_title=title)
        order_submenu = view_menu.order_submenu()

        if (order_submenu == "by alphabetical order (a -> z)"):
            Cli.cli_entry(title)
            PlayerController.display_alphabetical_p_atoz(None, players_list)
            GameController.return_to_main(title)
            Cli.cli_delay_no_interaction()

        elif (order_submenu == "by alphabetical order (z -> a)"):
            Cli.cli_entry(title)
            PlayerController.display_alphabetical_p_ztoa(None, players_list)

            Cli.cli_delay_no_interaction()

        elif (order_submenu == "by rank order (1 -> x)"):
            Cli.cli_entry(title)
            PlayerController.display_rank_p_1tox(None, players_list)
            GameController.return_to_main(title)
            Cli.cli_delay_no_interaction()

        elif (order_submenu == "by rank order (x -> 1)"):
            Cli.cli_entry(title)
            PlayerController.display_rank_p_xto1(None, players_list)
            GameController.return_to_main(title)
            Cli.cli_delay_no_interaction()

        elif (order_submenu == "return to reports menu"):
            Cli.cli_entry(title)
            GameController.reports_submenu(title)
            Cli.cli_clear()

    def return_to_main(title):
        view_menu = MainMenu(app_title=title)
        return_submenu = view_menu.return_to_main()

        if (return_submenu == 'True'):
            Cli.cli_clear()
            GameController(title)
        else:
            pass
