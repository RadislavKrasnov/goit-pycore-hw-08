"""Birthday entrity in address book."""

from datetime import datetime
from .field import Field

class Birthday(Field):
    """Represents birthday field in the address book's record."""

    def __init__(self, value: str) -> None:
        """Initializes the instance with birth date.
        
        Args:
            value:
                String with birthday in formay DD.MM.YYYY.

        Returns:
            None.

        Raises:
            ValueError: if date is invalid format.
            TypeError: if argument is missed.
        """
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
