# tournament_controller.py
# Created Sep 20, 2021 at 13:00 CEST
# Last updated Sep 20, 2021 at 13:00 CEST

# Standard imports

# Third-party imports

# Local imports
from models.player_model import Player
from views.cli_view import Cli
from models.match_model import Match
from models.rounds_model import Round
from views.menu import Menu
from controllers.match_controller import MatchController


# Other imports


class RoundController():

    def first_round(tournament_id):
        matchmaking = MatchController.matchmaking_first_round(tournament_id)
        matches_list = MatchController.matches_list_round(matchmaking)
        r_doc_id = RoundController.create_round(matches_list, 1)
        return r_doc_id

    def round(r_doc_id, i):
        # Get Round with doc_id
        round = Round.get_round_with_doc_id(r_doc_id)

        # Get matches list from first round
        matches_in_round = round['matches_list']

        # Get matches with docid in matches_in_round
        last_round_matches = []
        for matches_doc_id in matches_in_round:
            matches = Match.get_matches_w_doc_id(matches_doc_id)
            last_round_matches.append(matches)

        # Convert matches into tuple
        tuple_list = []
        for match in last_round_matches:
            deserialized = Match.deserialize_matches(match)
            tuple = Match.create_match_tuple(deserialized)
            print(tuple)
            tuple_list.append(tuple)
        print(tuple_list)

        # Sort p_one & p_two with scores in round
        matches = []
        for tuple in tuple_list:
            for match in tuple:
                matches.append(match)
        matches_sorted = matches.sort(key=lambda x: x[1])
        print(matches_sorted)
        length = len(matches_sorted)

        # if scores are equals sort with name
        unique_scores = []
        existing_scores = []

        print("Loop to check if match score already exists")
        for i in range(length):
            result = True

            # Get Score of a match
            match_score = matches_sorted[i][1]

            # List all scores
            scores_list = []
            for score in matches_sorted:
                scores_list.append(score[1])

            # Remove current score
            scores_list.remove(match_score)

            # Compare all the score with the selected match score
            for score in scores_list:
                if match_score == score:
                    result = True
                    break
                else:
                    result = False

            if not result:
                unique_scores.append(matches_sorted[i])
            else:
                existing_scores.append(matches_sorted[i])

        print("Unique")
        print(unique_scores)
        print("Existing")
        print(existing_scores)

        # matchmaking
        matches_list = []

        # Create Match
        next_r_doc_id = RoundController.create_round(matches_list, i)
        return next_r_doc_id

    def create_round(matches_list, round_number):
        round_name = Round.round_name(round_number)
        start_time = Round.start_round()
        round = Round(round_name, round_number, matches_list, start_time)
        r_doc_id = Round.create_round(round)
        return r_doc_id

    def attribute_results_round(title, r_doc_id):
        menu = Menu(app_title=title)
        print("Attribute results to Match")

        # Append Match in choices form
        round = Round.get_round_with_doc_id(r_doc_id)
        for match_doc_id in round['matches_list']:
            match = Match.get_matches_w_doc_id(match_doc_id)

            # Get Player with DOC ID
            player1 = match['p_one']
            player1_i = Player.get_player_with_doc_id(player1)
            player2 = match['p_two']
            player2_i = Player.get_player_with_doc_id(player2)

            menu.attribute_results_form[0]['choices'].append(
                {
                    'key': 'm',
                    'name': '{} {} ({}) vs {}  {} ({})'
                    .format(player1_i['name'],
                            player1_i['first_name'],
                            match['p_one_score'],
                            player2_i['name'],
                            player2_i['first_name'],
                            match['p_two_score']),
                    'value': match_doc_id
                }
            )

        answers = menu.attribute_results()
        match_results = answers['match_results']

        if answers['confirm']:
            MatchController.ask_winner(title, match_results)
            if answers['confirm']:
                Cli.cli_entry(title)
                RoundController.end_round_menu(None, title, r_doc_id)
                Cli.clear_screen()

    def end_round_menu(self, title, r_doc_id):
        menu = Menu(app_title=title)
        answers = menu.end_round()

        if not answers['confirm']:
            RoundController.attribute_results_round(title, r_doc_id)

        elif answers['confirm']:
            pass
