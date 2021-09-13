# tournament_controller.py
# Created Sep 10, 2021 at 11:10
# Last Updated Sep 13, 2021 at 15:12

# Standrad imports

# local imports
from models.player_model import Player
from models.tournament_model import Tournament
from views.menu import Menu

# Other imports


class TournamentController():

    """ Summary of Methods used in Tournament Controller

    - Methods :
        tournament_creation_menu(self, title)
            This method is used to manage tournament creation menu.
            Display menu, manage answers &
            save the tournaments in 'tournaments' DB.
    """

    def tournament_creation_menu(self, title):
        tournament_menu = Menu(app_title=title)
        print("Add a tournament to the 'tournaments' DB.")

        # Append choices with players list
        display_p = Player.load_players_db()
        tournament_menu.tournament_form[7]['choices'] = []
        for player in display_p:
            tournament_menu.tournament_form[7]['choices'].append(
                {
                    'name': "{} {} (rank {})".format(player['first_name'],
                                                     player['name'],
                                                     player['rank'])
                },
            )

        # Display form + saves it in DB
        answers = tournament_menu.tournament_menu()
        if answers['confirm']:
            obj = Tournament.deserialize_tournament(answers)
            obj.create_tournament()

    def display_tournaments(self):
        print("List of tournaments sorted in alphabetical order")
        tournaments_list = Tournament.load_tournaments_db()
        for tournament in tournaments_list:
            obj = Tournament.deserialize_tournament(tournament)
            print(obj)

    def launch_tournament(self, title):
        launch = Menu(app_title=(title))
        print("You can now modify a player rank in 'players' DB.")

        # Append Choices with tournaments list
        display_t = Tournament.load_tournaments_db()
        for tournament in display_t:
            launch.launch[0]['choices'].append(tournament['name'])

        # Getting Player doc_id
        answers = launch.launch_tournament_menu()
        if answers['confirm']:
            obj = Tournament.get_tournament_w_name(answers['selected_t'])
            print(obj)
            return obj
