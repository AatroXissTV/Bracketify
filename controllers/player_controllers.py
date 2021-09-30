# controllers/player_controllers.py
# created 23/09/2021 @ 00:34 CEST
# last updated 28/09/2021 @ 12:00 CEST

""" controllers/player_controller.py

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
from models.player_models import Player
from views.cli_views import Cli
from views.player_views import PlayerMenu

# other


class PlayerController():
    """this class represents the player controller of Bracketify

    Manages menus that are player related
    """

    def add_a_new_player_menu(title):
        Cli.cli_entry(title)
        player_menus = PlayerMenu(app_title=title)
        print("You can now add a new player in the 'players' DB.")
        print("Please enter the requested information\n")

        answers = player_menus.add_a_new_player()

        if answers['confirm']:
            obj = Player.deserialize_player(answers)
            obj.create_player()
            Cli.cli_delay()
        else:
            print("\nThe player has not been added to the database\n")
            Cli.cli_delay_no_interaction()
            pass

    def modify_player_rank_menu(title):
        Cli.cli_entry(title)
        player_menus = PlayerMenu(app_title=title)
        print("You can now update a player rank in the 'players' DB.")
        print("Please enter the requested information\n")

        # Load player in choices.
        players_docid_list = Player.load_players_docid_db()
        for player_docid in players_docid_list:
            player = Player.get_player_w_docid(player_docid)
            player_menus.modify_rank_form[0]['choices'].append(
                {
                    'key': 'p',
                    'name': '{} {} ({})'
                    .format(player['name'],
                            player['first_name'],
                            player['rank']),
                    'value': player_docid
                }
            )

        answers = player_menus.modify_rank()
        if answers['confirm']:
            obj = Player.update_player_rank(None, answers['new_rank'],
                                            answers['doc_id'])
            Cli.cli_delay()
            return obj
        else:
            print("\nThe player rank has not been modified\n")
            Cli.cli_delay_no_interaction()
            pass

    def modify_player_in_t_rank(title, ordered_list):
        player_menus = PlayerMenu(app_title=title)
        print("You can now modify player rank.")

        # Load player in ordered_list in choices
        for player_docid in ordered_list:
            player = Player.get_player_w_docid(player_docid[0])
            player_menus.modify_rank_form[0]['choices'].append(
                {
                    'key': 'p',
                    'name': '{} {} ({})'
                    .format(player['name'],
                            player['first_name'],
                            player['rank']),
                    'value': player_docid[0]
                }
            )
        answers = player_menus.modify_rank()
        if answers['confirm']:
            obj = Player.update_player_rank(None, answers['new_rank'],
                                            answers['doc_id'])
            answers = player_menus.return_to_menu()
            if answers['confirm']:
                pass
            else:
                PlayerController.modify_player_in_t_rank(title, ordered_list)
            return obj
        else:
            PlayerController.modify_player_in_t_rank(title, ordered_list)
            pass

    # DISPLAY

    def display_players(title):
        Cli.cli_entry(title)
        print("List of all players in DataBase\n")
        players_docid_list = Player.load_players_docid_db()
        players_list = []
        for player_docid in players_docid_list:
            player = Player.get_player_w_docid(player_docid)
            players_list.append(player)
        return players_list

    # DISPLAY ORDER

    def display_alphabetical_p_atoz(title, players_list):
        Cli.cli_entry(title)
        print("List of players sorted in alphabetical order")
        print("(a -> z)\n")
        sorted_players_atoz = Player.get_players_ordered_by_name(players_list,
                                                                 False)
        for player in sorted_players_atoz:
            obj = Player.deserialize_player(player)
            print(obj)

    def display_alphabetical_p_ztoa(title, players_list):
        Cli.cli_entry(title)
        print("List of players sorted in alphabetical order")
        print("(z -> a)\n")
        sorted_players_ztoa = Player.get_players_ordered_by_name(players_list,
                                                                 True)
        for player in sorted_players_ztoa:
            obj = Player.deserialize_player(player)
            print(obj)

    def display_rank_p_1tox(title, players_list):
        Cli.cli_entry(title)
        print("List of players sorted in rank order")
        print("(1 -> x)\n")
        sorted_players_1tox = Player.get_players_ordered_by_rank(players_list,
                                                                 False)
        for player in sorted_players_1tox:
            obj = Player.deserialize_player(player)
            print(obj)

    def display_rank_p_xto1(title, players_list):
        Cli.cli_entry(title)
        print("List of players sorted in rank order")
        print("(1 -> x)\n")
        sorted_players_xto1 = Player.get_players_ordered_by_rank(players_list,
                                                                 True)
        for player in sorted_players_xto1:
            obj = Player.deserialize_player(player)
            print(obj)
