# views/round_views.py
# created 24/09/2021 @ 16:24 CEST
# last updated 28/09/2021 @ 11:06 CEST

# must be at the beginning of the file
from __future__ import print_function, unicode_literals

""" views/round_views.py

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
from PyInquirer import style_from_dict, Token, prompt

# local imports
from views.cli_views import Cli

# other


class RoundMenu(Cli):
    """This class represents the round menu of Bracketify

    - Herit from Cli (cli_views.py)
    """

    def __init__(self, app_title):
        super().__init__(app_title)
        """Constructor

        app_title -> str
        """

        self.style = style_from_dict({
            Token.Answer: '#568259',
            Token.Question: '',  # Default
            Token.Instruction: '#E63946',
            Token.Pointer: '#F1FAEE'
        })

        self.start_round_form = [
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Do you want to start the round ?',
                'default': False,
            }
        ]

        self.attribute_results_form = [
            {
                'type': 'list',
                'name': 'match_results',
                'message': "To which match do you want to attribute a result?",
                'choices': []
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Do you want to attribute score to this match?',
                'default': True,
            },
        ]

        self.ask_winner_form = [
            {
                'type': 'list',
                'name': 'ask_winner',
                'message': "Select Winner (tie = 0, P1 = 1, P2 = 2)",
                'choices': ['0', '1', '2']
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False,
            }
        ]

        self.end_round_form = [
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Do you want to end the round ?',
                'default': False,
            }
        ]

        self.results_form = [
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Do you want to return to main menu',
                'default': False,
            }

        ]

    """Method used in RoundMenu Class

    - Methods:
        start_round(self):
            used to prompt a from and start a round

        attribute_results(self):
            used to prompt attribute results form.
    """

    def start_round(self):
        start_round = self.start_round_form
        answers = prompt(start_round, style=self.style)
        return answers

    def attribute_results(self):
        display_match = self.attribute_results_form
        answers = prompt(display_match, style=self.style)
        return answers

    def ask_winner(self):
        ask_winner = self.ask_winner_form
        answers = prompt(ask_winner, style=self.style)
        return answers['ask_winner']

    def end_round(self):
        end_round = self.end_round_form
        answers = prompt(end_round, style=self.style)
        return answers

    def results(self):
        results_form = self.results_form
        answers = prompt(results_form, style=self.style)
        return answers
