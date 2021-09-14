# tournament_controller.py
# Created Sep 10, 2021 at 11:10
# Last Updated Sep 14, 2021 at 10:28

# Standrad imports

# local imports
from models.rounds_model import Round
from models.match_model import Match
from models.player_model import Player
from models.tournament_model import Tournament
from views.menu import Menu

# Other imports


class TournamentController():

    """ Summary of Methods used in Tournament Controller

    - Methods :
        create_tournament(self, title)
            This method is used to manage creation of tournaments.
            Display menu, manage answers &
            save the tournaments in 'tournaments' DB.
    """

    def create_tournament(self, title):
        tournament_menu = Menu(app_title=title)
        print("Add a tournament to the 'tournaments' DB.")

        # Append choices with players list
        display_p = Player.load_players_db()

        for player in display_p:

            # Value is DOC ID of a player
            doc_id = Player.get_player_doc_id(player['name'])

            tournament_menu.tournament_form[7]['choices'].append(
                {
                    'key': 'd',
                    'name': '{} {} (rank {})'.format(player['first_name'],
                                                     player['name'],
                                                     player['rank']),
                    'value': doc_id,
                },
            )

        # prompt form + saves it in DB
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
        print("Launch a tournament.")

        # Append Choices with tournaments list
        display_t = Tournament.load_tournaments_db()
        for tournament in display_t:
            launch.launch[0]['choices'].append(tournament['name'])

        answers = launch.launch_tournament_menu()

        if answers['confirm']:
            t = Tournament.get_tournament_w_name(answers['selected_t'])
            i = t['players_list']
            player_list = []
            for player in i:
                test = Player.get_player_with_doc_id(player)
                player_list.append(test)
            display_rank_p = Player.get_players_ordered_by_rank(player_list)

            length = len(display_rank_p)
            middle_index = length//2

            first_half = display_rank_p[:middle_index]
            second_half = display_rank_p[middle_index:]

            print("Generating matches for the first round...")
            matches_list = []
            for i in range(middle_index):
                test = Match(first_half[i]['first_name'],
                             second_half[i]['first_name'])
                print(test)
                serialized = test.serialize_match()
                matches_list.append(serialized)

            start_time = Round.start_round()
            test2 = Round("Round", 1, matches_list, start_time)
            print(test2)

            print("Who won the first match ?")
            matches_list[0]
            testencore = test.match_results("0")
            print(testencore)
