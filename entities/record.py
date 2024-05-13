"""Record module."""

from .name import Name
from .phone import Phone
from .birthday import Birthday

class Record:
    """Represents a record in the address book.
    
    Attributes:
        name:
            Name object with contact's name as a value.
        phones:
            List of Phone objects.
    """

    def __init__(self, name: str) -> None:
        """Initializes Record instace based on contact's name.
        
        Args:
            name:
                Name object with contact's name as a value.

        Raises:
            TypeError: if name argument is missed
        """
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self) -> str:
        """Returns human readable information of the object.
        
        Returns:
            String with information about object.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str) -> None:
        """Adds phone in the list on phones
        
        Args:
            phone_number:
                String with phone number. Must contain 10 digits.
        
        Returns:
            None.
        
        Raises:
            PhoneValidationError: if invalid format of phone number is passed.
            TypeError: if no argument passed or argument isn't string.
        """
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str) -> None:
        """Removes phone number from the address book record.

        Args:
            phone_number:
                String with phone number.
        
        Returns:
            None.

        Raises:
            TypeError: if no argument passed.
        """
        index = next((i for i, item in enumerate(self.phones) if item.value == phone_number), -1)

        if index != -1:
            del self.phones[index]

    def edit_phone(self, current_number: str, new_number: str) -> None:
        """Edits phone number in the address book record.
        
        Args:
            current_number:
                String with current phone number.
            new_number:
                String with new number phone number.

        Returns:
            None.
        
        Raises:
            TypeError: if no argument passed.
            ValueError: if current_number doesn't exist.
            PhoneValidationError: if phone number less then 10 digits.
        """
        index = next((i for i, item in enumerate(self.phones) if item.value == current_number), -1)

        if index != -1:
            self.phones[index] = Phone(new_number)
        else:
            raise ValueError('No such phone in the record')


    def find_phone(self, phone_number: str) -> None:
        """Finds phone number from the address book record phones list.
        
        Args:
            phone_number:
                String with phone number to find.

        Returns:
            String with phone number. Otherwise it returns None if phone number wasn't found.

        Raises:
            TypeError: if no argument passed.
        """
        return next((item for item in self.phones if item.value == phone_number), None)

    def add_birthday(self, birth_date: str) -> None:
        """Adds birthday to the address book record.
        
        Args:
            birth_date:
                String in format DD.MM.YYYY.
        
        Returns:
            None.

        Raises:
            ValueError: if date string is invalid format.
            TypeError: if argument is missed. 
        """
        self.birthday = Birthday(birth_date)
