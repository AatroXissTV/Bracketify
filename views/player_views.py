# views/player_views.py
# created 23/09/2021 @ 00:40 CEST
# last updated 28/09/2021 @ 10:40 CEST

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
from views.validators_views import DateValidator
from views.validators_views import StringValidator
from views.validators_views import NumberValidator


# other


class PlayerMenu(Cli):
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

        self.add_a_new_player_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'last name: ',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'first_name',
                'message': 'first name: ',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'birth_date',
                'message': 'birth date: ',
                'validate': DateValidator
            },
            {
                'type': 'list',
                'name': 'gender',
                'message': 'gender: ',
                'choices': ['Male',
                            'Female',
                            'Other'],
                'default': 'Other'
            },
            {
                'type': 'input',
                'name': 'rank',
                'message': 'rank: ',
                'validate': None,
                'filter': lambda val: int(val) if int(val) > 0 else None
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure you want to validate these fields?',
                'default': False,
            },
        ]

        self.modify_rank_form = [
            {
                'type': 'list',
                'name': 'doc_id',
                'message': 'Select the player you want to edit: ',
                'choices': [],
            },
            {
                'type': 'input',
                'name': 'new_rank',
                'message': 'Enter the new rank: ',
                'validate': NumberValidator,
                'filter': lambda val: int(val) if int(val) > 0 else None
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure you want to validate these fields?',
                'default': False,
            },
        ]

        self.return_to_menu_form = [
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'return to main menu (Y) or modify ranks (n)',
                'default': True,
            }
        ]

    """Summary of methods and quick explanation

    - Methods:
        add_a_new_player(self):
            prompt new player form to the user
            return True or False

        modify_rank(self):
            prompt modify rank form
    """

    def add_a_new_player(self):
        add_a_new_player_form = self.add_a_new_player_form
        answers = prompt(add_a_new_player_form, style=self.style)
        return answers

    def modify_rank(self):
        modify_rank_form = self.modify_rank_form
        answers = prompt(modify_rank_form, style=self.style)
        return answers

    def return_to_menu(self):
        return_to_menu_form = self.return_to_menu_form
        answers = prompt(return_to_menu_form, style=self.style)
        return answers
