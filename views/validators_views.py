# views/validators_views.py
# created 23/09/2021 @ 00:51 CEST
# last updated 23/09/2021 @ 00:51 CEST

""" views/validators_views.py

To do:
    * Update requirements with dateparser
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.5.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports
from dateparser import parse

# third-party imports
from PyInquirer import Validator, ValidationError

# local imports

# other


class DateValidator(Validator):
    """ Validator for dates.
    """

    def validate(self, document):
        try:
            assert is_date(document.text)
        except (ValueError, AssertionError):
            raise ValidationError(
                message="please, enter a valid date",
                cursor_position=len(document.text)
            )
        return super().validate(document)


def is_date(string) -> bool:
    """Return whether the string can be considered as date
    """

    return bool(parse(string, settings={
        'DATE_ORDER': 'DMY',
        'STRICT_PARSING': True
    }))
