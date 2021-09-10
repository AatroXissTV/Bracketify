# tournament_controller.py
# Created Sep 10, 2021 at 11:10
# Last updated Sep 10, 2021 at 11:10

# Standrad imports

# local imports
from models.player_model import Player
from models.tournament_model import Tournament
from views.main_menu import MainMenu

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
        tournament_menu = MainMenu(app_title=title)
        print("Add a tournament to the 'tournaments' DB.")

        # Append choices wit players list
        display_p = Player.load_players_db()
        tournament_menu.tournament_form[7]['choices'] = []
        for player in display_p:
            tournament_menu.tournament_form[7]['choices'].append(
                {
                    'name': "{} {} (rank {})".format(player['first_name'],
                                                     player['name'],
                                                     player['rank'])
                }
            )

        # Display form + saves it in DB
        answers = tournament_menu.tournament_menu()
        if answers['confirm']:
            obj = Tournament.deserialize_tournament(answers)
            obj.create_tournament()

    def display_tournaments(self):
        print("List of players sorted in alphabetical order")
        tournaments_list = Tournament.load_tournaments_db()
        tournaments = []
        for tournament in tournaments_list:
            tournaments.append(tournament)
        print(tournaments)
