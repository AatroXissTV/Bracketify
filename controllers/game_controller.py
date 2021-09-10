# game_controller.py
# Created Sep 07, 2021 at 11:19
# Last updated Sep 08, 2021 at 16:06

# Standard imports

# Third-party imports

# Local imports
from views.cli_view import Cli
from views.main_menu import MainMenu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

# Other imports


class GameController():
    """Represents the game controller
    """

    def __init__(self, app_title):
        """ Constructor

        - Args:
            app_title
                Used to retrieve app name.
        """
        self.app_title = app_title

    """Summary of Methods used in Game controller

    - Static Methods :
        cli_entry(app_title):
            Method is used to manage cli (clear screen + display title)
        cli_exit_with_delay(app_title):
            Method is used to exit cli (delay)
        cli_exit(app_title):
            Method is used to exit cli
    """

    def start(self):
        title = self.app_title
        view_menu = MainMenu(app_title=title)

        while (view_menu != 'Quit'):
            Cli.cli_entry(title)
            menu = view_menu.main_menu()
            if (menu == 'Add a player'):
                Cli.cli_entry(title)
                PlayerController.player_creation_menu(None, title)
                Cli.cli_exit_with_delay(title)

            elif (menu == 'Modify a player rank'):
                Cli.cli_entry(title)
                PlayerController.update_player_rank_menu(None, title)
                Cli.cli_exit_with_delay(title)

            elif (menu == 'Add a tournament'):
                Cli.cli_entry(title)
                TournamentController.tournament_creation_menu(None, title)
                Cli.cli_exit_with_delay(title)

            elif (menu == 'Launch a tournament'):
                Cli.cli_entry(title)
                print("Select the tournament you wanna launch")
                view_menu.launch_tournament_menu()
                Cli.cli_exit_with_delay(title)

            elif (menu == 'Display Infos'):
                GameController.submenu(title)

            elif (menu == 'Quit'):
                Cli.cli_exit(title)
                view_menu.quit_menu()

    def submenu(title):
        menus = MainMenu(app_title=title)
        submenu = menus.display_menus_item()

        if (submenu == 'Players'):
            Cli.cli_entry(title)
            GameController.subsubmenu(title)

        elif (submenu == 'Tournaments'):
            Cli.cli_entry(title)
            TournamentController.display_tournaments(None)
            GameController.subsubsubmenu(title)

        elif (submenu == 'Return'):
            Cli.cli_entry(title)
            GameController.start()

    def subsubmenu(title):
        menus = MainMenu(app_title=title)
        print('How do you want to display Datas?')
        subsubmenu = menus.sort_menus_items()

        if (subsubmenu == 'By alphabetical order (a -> z)'):
            Cli.cli_entry(title)
            PlayerController.display_aplhabetical_player(None)
            GameController.subsubsubmenu(title)

        elif (subsubmenu == 'By rank order (1 -> x)'):
            Cli.cli_entry(title)
            PlayerController.display_rank_player(None)
            GameController.subsubsubmenu(title)

        elif (subsubmenu == 'Return'):
            Cli.cli_entry(title)
            GameController.submenu(title)

    def subsubsubmenu(title):
        menus = MainMenu(app_title=title)
        subsubsubmenu = menus.return_to_main()

        if (subsubsubmenu == 'True'):
            GameController.start()
