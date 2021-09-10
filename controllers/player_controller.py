# player_controller.py
# Created Sep 10, 2021 at 10:00
# Last Updated Sep 10, 2021 at 15:12

# Standard imports

# Third-Party imports

# Local imports
from models.player_model import Player
from views.main_menu import MainMenu

# Other imports


class PlayerController():

    """ Summary of Methods used in Player Controller.

    - Methods :
        player_creation_menu(self):
            This method is used to manage creation player menu.
            Display menu, Manage answers & Save the new player in 'players' DB.
        update_player_rank_menu(self):
            This method is used to manage updates to ranks.
            Display menu, manage answers & Save the new rank.

    """

    def player_creation_menu(self, title):
        player_menu = MainMenu(app_title=title)
        print("You can now add a new player in the 'players' DB.")
        answers = player_menu.player_menu()
        if answers['confirm']:
            obj = Player.deserialize_player(answers)
            obj.create_player()

    def update_player_rank_menu(self, title):
        update_rank = MainMenu(app_title=(title))
        print("You can now modify a player rank in 'players' DB.")

        # Append Choices with Players list
        display_p = Player.load_players_db()
        for player in display_p:
            update_rank.modify_rank_form[0]['choices'].append(player['name'])

        # Update Rank Menu & Getting Player doc_id
        answers = update_rank.modify_rank_menu()
        if answers['confirm']:
            doc_id = Player.get_player_doc_id(answers['name'])
            obj = Player.update_player_rank(None, answers['new_rank'],
                                            doc_id)
            return obj

    def display_aplhabetical_player(self):
        print("List of players sorted in alphabetical order")
        list = Player.load_players_db()
        display_alphabetical_p = Player.get_players_ordered_by_name(list)
        for player in display_alphabetical_p:
            obj = Player.deserialize_player(player)
            print(obj)

    def display_rank_player(self):
        print("List of players sorted in rank order")
        list = Player.load_players_db()
        display_alphabetical_p = Player.get_players_ordered_by_rank(list)
        for player in display_alphabetical_p:
            obj = Player.deserialize_player(player)
            print(obj)
