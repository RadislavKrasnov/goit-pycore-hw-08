"""Phone entrity in address book."""

import re
from .field import Field
from exceptions import PhoneValidationError

class Phone(Field):
    """Represents phone field in the address book's record."""
    
    def __init__(self, value: str) -> None:
        """Initializes the instance with phone number.
        Validates phone number for 10 digits.

        Args:
            value:
                String with phone number.

        Returns:
            None.

        Raises:
            TypeError: if argument isn't passed or isn't a string.
            PhoneValidationError: if phone number string doesn't contain 10 digits.
        """
        match = re.match(r"^\d{10}$", value)

        if match:
            super().__init__(value)
        else:
            raise PhoneValidationError('Phone number should have 10 digits!')
