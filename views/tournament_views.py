# views/tournament_views.py
# created 23/09/2021 @ 11:46 CEST
# last updated 28/09/2021 @ 11:00 CEST

# must be at the beginning of the file
from __future__ import print_function, unicode_literals

""" views/tournament_views.py

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
from views.validators_views import DateValidator, NumberValidator
from views.validators_views import StringValidator

# other


class TournamentMenu(Cli):
    """This class represents player menus of Bracketify

    - Herit from Cli (cli_views.py)
    """

    def __init__(self, app_title):
        super().__init__(app_title)
        """Constructor

        app_title ->str
        """

        self.style = style_from_dict({
            Token.Answer: '#568259',
            Token.Question: '',  # Default
            Token.Instruction: '#E63946',
            Token.Pointer: '#F1FAEE'
        })

        self.add_a_tournament_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': "Enter the tournament's name: ",
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'location',
                'message': "location",
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'start_date',
                'message': 'Start date',
                'validate': DateValidator
            },
            {
                'type': 'input',
                'name': 'end_date',
                'message': 'End date',
                'validate': DateValidator
            },
            {
                'type': 'input',
                'name': 'description',
                'message': 'Comments: '
            },
            {
                'type': 'list',
                'name': 'rules',
                'message': 'Select the tournaments rules',
                'choices': ["Bullet", "Blitz", "Rapid"]
            },
            {
                'type': 'input',
                'name': 'rounds_number',
                'message': "Numb of rounds > 0 or set to 4",
                'default': '4',
                'validate': NumberValidator,
                'filter': lambda val: int(val) if int(val) > 0 else None
            },
            {
                'type': 'checkbox',
                'message': 'Select players participating (8 min)',
                'name': 'players_list',
                'choices': [],
                'validate': lambda choices: 'Select 8 players min'
                if len(choices) < 8 else True,
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure you want to validate these fields?',
                'default': False,
            },
        ]

        self.select_tournament_form = [
            {
                'type': 'list',
                'name': 'selected_t',
                'message': 'Select the tournament: ',
                'choices': [],
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure you want to validate these fields?',
                'default': False,
            },
        ]

    """Summary of methods and quick explanation

    - Methods:
        add_a_new_tournament(self):
            prompt new tournament form to the user

        select_tournament(self):
            prompt tournament selection form to the user
    """

    def add_a_new_tournament(self):
        add_a_new_tournament_form = self.add_a_tournament_form
        answers = prompt(add_a_new_tournament_form, style=self.style)
        return answers

    def select_tournament(self):
        select_tournament_form = self.select_tournament_form
        answers = prompt(select_tournament_form, style=self.style)
        return answers
