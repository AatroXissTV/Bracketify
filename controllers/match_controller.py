# match_controller.py
# Created Sep 16, 2021 at 10:30
# Last Updated Sep 17, 2021 at 10:30

# Standard imports

# Local imports
from models.match_model import Match
from views.menu import Menu

# Other imports


class MatchContoller():

    def ask_winner(title, match_selected):
        print("Enter the winner of the round")
        menu = Menu(app_title=title)

        ask_winner_menu = menu.ask_winner()

        if (ask_winner_menu == "0"):
            i = ask_winner_menu
            match_results = MatchContoller.update_scores(match_selected,
                                                         i)
            print(match_results)

        elif (ask_winner_menu == "1"):
            i = ask_winner_menu
            match_results = MatchContoller.update_scores(match_selected,
                                                         i)
            print(match_results)

        elif (ask_winner_menu == "2"):
            i = ask_winner_menu
            match_results = MatchContoller.update_scores(match_selected,
                                                         i)
            print(match_results)

        return match_results

    def update_scores(match_selected, i):
        get_match = Match.get_matches_w_doc_id(match_selected)
        match_object = Match.deserialize_matches(get_match)
        match_object.match_results(i)
        serialized_match = match_object.serialize_match()
        match_object.update_scores(serialized_match['p_one_score'],
                                   serialized_match['p_two_score'],
                                   match_selected)
        return match_object
