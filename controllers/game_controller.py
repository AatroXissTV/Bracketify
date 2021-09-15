# game_controller.py
# Created Sep 07, 2021 at 11:19 CEST
# Last Updated Sep 15, 2021 at 14:00 CEST

# Standard imports

# Third-party imports

# Local imports
from models.player_model import Player
from views.cli_view import Cli
from views.menu import Menu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

# Other imports


class GameController():
    """Represents the game controller

    This controller manages the menu logic
    and calls each dedicated controllers when needed.
    """

    def __init__(self, app_title):
        """ Constructor

        - Args:
            app_title
                Used to retrieve app name from main.py
        """

        self.app_title = app_title

    """Summary of Methods used in Game controller

    - Methods :
        start(self):
            This method represents the main menu of the programm.

                Calls:
                It calls other methods within GameController
                to navigate between submenus.

                For each menu it calls the appropriate controller.
                -> PlayerController -> Everything related to players.
                -> TournamentController -> Everything related to tournaments.

        display_submenu(title):
            This method is used to manage submenu for the display options.

                Calls :
                For each menu item it calls the appropriate controller.
                -> PlayerController
                -> TournamentController

        order_submenu(title):
            This method is used to manage order in displays for
            tournaments and players.

        return_submenu(title):
            This method is used to manage return to main submenu
            after displaying datas
    """

    # Starting MAIN MENU

    def start(self):
        title = self.app_title
        view_menu = Menu(app_title=title)

        while (view_menu != 'Quit'):
            Cli.cli_entry(title)
            menu = view_menu.main_menu()

            if (menu == 'Add a player'):
                Cli.cli_entry(title)
                PlayerController.player_creation_menu(None, title)
                Cli.cli_delay()

            elif (menu == 'Modify a player rank'):
                Cli.cli_entry(title)
                PlayerController.update_player_rank_menu(None, title)
                Cli.cli_delay()

            elif (menu == 'Add a tournament'):
                Cli.cli_entry(title)
                TournamentController.create_tournament(None, title)
                Cli.cli_delay()

            elif (menu == 'Launch a tournament'):
                Cli.cli_entry(title)
                TournamentController.launch_tournament(None, title)
                Cli.cli_delay()

            elif (menu == 'Display Infos'):
                GameController.display_submenu(title)

            elif (menu == 'Quit'):
                Cli.clear_screen()
                view_menu.quit_menu()

    # DISPLAY SUBMENU

    def display_submenu(title):
        menus = Menu(app_title=title)
        display_submenu = menus.display_menus_item()

        if (display_submenu == 'Players'):
            Cli.cli_entry(title)
            players_list = Player.load_players_db()
            GameController.order_submenu(title, players_list)

        elif (display_submenu == 'Tournaments'):
            Cli.cli_entry(title)
            TournamentController.display_tournaments(None)
            GameController.return_submenu(title)

        elif (display_submenu == 'Players in tournaments'):
            Cli.cli_entry(title)
            p_list = TournamentController.display_player_in_t(None, title)
            Cli.cli_entry(title)
            GameController.order_submenu(title, p_list)
            GameController.return_submenu(title)

        elif (display_submenu == 'Return'):
            Cli.cli_entry(title)
            GameController(title)

    # ORDER SUBMENU

    def order_submenu(title, players_list):
        menus = Menu(app_title=title)
        order_submenu = menus.sort_menus_items()

        if (order_submenu == 'By alphabetical order (a -> z)'):
            Cli.cli_entry(title)
            PlayerController.display_aplhabetical_player(None, players_list)
            GameController.return_submenu(title)

        elif (order_submenu == 'By rank order (1 -> x)'):
            Cli.cli_entry(title)
            PlayerController.display_rank_player(None, players_list)
            GameController.return_submenu(title)

        elif (order_submenu == 'Return'):
            Cli.cli_entry(title)
            GameController.order_submenu(title)

    # RETURN TO MAIN SUBMENU

    def return_submenu(title):
        menus = Menu(app_title=title)
        subsubsubmenu = menus.return_to_main()

        if (subsubsubmenu == 'True'):
            Cli.clear_screen(title)
            GameController(title)
