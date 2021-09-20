# tournament_controller.py
# Created Sep 20, 2021 at 13:00 CEST
# Last updated Sep 20, 2021 at 13:00 CEST

# Standard imports

# Third-party imports

# Local imports
from views.menu import Menu
from models.player_model import Player
from models.tournament_model import Tournament
from models.match_model import Match


# Other imports


class MatchController():

    def matchmaking_first_round(tournament_id):
        players_list = Tournament.get_players_in_t(tournament_id)
        ordered_player = Player.get_players_ordered_by_rank(players_list)
        ordered_doc_id = []
        for player in ordered_player:
            doc_id = Player.get_player_doc_id(player['name'])
            ordered_doc_id.append(doc_id)
        matchmaking = MatchController.matches_first_round(ordered_doc_id)
        return matchmaking

    def matches_first_round(ordered_players):
        middle_index = Match.middle_index_players_list(ordered_players)
        first_half = Match.split_first_half(ordered_players, middle_index)
        second_half = Match.split_second_half(ordered_players, middle_index)
        mm = Match.mm_first_round(middle_index,
                                  first_half,
                                  second_half)
        return mm

    def matches_list_round(mm):
        matches_list = []
        for matches in mm:
            deserialized = Match.deserialize_matches(matches)
            match_doc_id = Match.create_match(deserialized)
            matches_list.append(match_doc_id)
        return matches_list

    def ask_winner(title, match_selected):
        menu = Menu(app_title=title)

        ask_winner_menu = menu.ask_winner()

        if (ask_winner_menu == "0"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            print(match)

        elif (ask_winner_menu == "1"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            print(match)

        elif (ask_winner_menu == "2"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            print(match)

    def update_scores(match_selected, i):
        get_match = Match.get_matches_w_doc_id(match_selected)
        match_object = Match.deserialize_matches(get_match)
        match_object.match_results(i)
        serialized_match = match_object.serialize_match()
        match_object.update_scores(serialized_match['p_one_score'],
                                   serialized_match['p_two_score'],
                                   match_selected)
        get_new_match = Match.get_matches_w_doc_id(match_selected)
        new_match = Match.deserialize_matches(get_new_match)
        return new_match
