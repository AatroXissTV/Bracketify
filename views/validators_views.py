# views/validators_views.py
# created 23/09/2021 @ 00:51 CEST
# last updated 28/09/2021 @ 10:40 CEST

""" views/validators_views.py

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


class StringValidator(Validator):
    """ Validator for strings
    """

    def validate(self, document):
        try:
            assert document.text
        except AssertionError:
            raise ValidationError(
                message="field is empty."
            )


class NumberValidator(Validator):
    """Validator for numbers
    """

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Enter a number',
                cursor_position=len(document.text))  # Move cursor to end
        try:
            assert int(document.text) > 0
        except AssertionError:
            raise ValidationError(
                message='Enter a number > 0',
                cursor_position=len(document.text))  # Move cursor to end


def is_date(string) -> bool:
    """Return whether the string can be considered as date
    """

    return bool(parse(string, settings={
        'DATE_ORDER': 'DMY',
        'STRICT_PARSING': True
    }))
