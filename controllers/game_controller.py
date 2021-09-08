# game_controller.py
# Created Sep 07, 2021 at 11:19
# Last updated Sep 08, 2021 at 16:06

# Standard imports

# Third-party imports

# Local imports
from models.player_model import Player
from models.tournament_model import Tournament
from views.cli_view import Cli
from views.main_menu import MainMenu


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

    - Methods :
        start(self):
            Method is used to display main menu to the user
    """

    def start(self):
        title = self.app_title
        view_menu = MainMenu(app_title=title)
        view_title = Cli(title)

        while view_menu != 'Quit':
            view_title.display_title()
            menu = view_menu.main_menu()
            if (menu == 'Add a player'):
                view_title.clear_screen()
                view_title.display_title()
                print("You can now add a new player in the 'players' DB.")
                answers = view_menu.player_menu()
                if answers['confirm']:
                    obj = Player.deserialize_player(answers)
                    obj.create_player()
                view_title.delay_new_screen()

            elif (menu == 'Modify a player rank'):
                view_title.clear_screen()
                view_title.display_title()
                print("You can now modify a player rank in 'players' DB.")

                display_players = Player.load_players_db()

                for player in display_players:
                    p_name = player['name']
                    view_menu.modify_rank_form[0]['choices'].append(p_name)

                answers = view_menu.modify_rank_menu()

                if answers['confirm']:
                    test_doc_id = Player.get_player_doc_id(answers['name'])
                    obj = Player.update_player_rank(None, answers['new_rank'],
                                                    test_doc_id)
                view_title.delay_new_screen()

            elif (menu == 'Add a tournament'):
                view_title.clear_screen()
                view_title.display_title()
                print("Add a tournament to the 'tournaments' DB.")

                display_players = Player.load_players_db()

                for player in display_players:
                    p_name = player['name']
                    view_menu.tournament_form[6]['choices'].append(p_name)

                answers = view_menu.tournament_menu()

                if answers['confirm']:
                    obj = Tournament.deserialize_tournament(answers)
                    obj.create_tournament()
                view_title.delay_new_screen()

            elif (menu == 'Launch a tournament'):
                view_title.clear_screen()
                view_title.display_title()
                print("Select the tournament you wanna launch")
                view_menu.launch_tournament_menu()
                view_title.delay_new_screen()

            elif (menu == 'Display Infos'):
                view_title.clear_screen()
                view_title.display_title()
                print("Display the info you wanna check")
                display_menu = view_menu.display_infos_menu()
                if (display_menu == 'All players'):
                    view_title.clear_screen()
                    view_title.display_title()
                    print("Here is the list of all the players.")
                    display_players = Player.load_players_db()
                    print(display_players)

            elif (menu == 'Quit'):
                view_title.clear_screen()
                view_menu.quit_menu()
