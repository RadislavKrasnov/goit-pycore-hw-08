"""Address book command handler."""

from .address_book import AddressBook
from .record import Record
from handlers import input_error_decorator

class CommandHandler:
    """Handles commands of address book bot."""

    @input_error_decorator()
    def add_contact(self, args: list, book: AddressBook) -> str:
        """Adds contact into address book.
        
        Args:
            args:
                List with name and phone.
            book:
                Object of address book.
        
        Returns:
            String with message.

        Raises:
            ValueError: Not enough values to unpack.
            PhoneValidationError: if phone number less then 10 digits.
        """
        name, phone, *_ = args
        record = book.find(name)
        message = "Contact updated."
        if record is None:
            record = Record(name)
            book.add_record(record)
            message = "Contact added."
        if phone:
            record.add_phone(phone)
        return message

    @input_error_decorator()
    def change_contact(self, args: list, book: AddressBook) -> str:
        """Changes contact.

        Args:
            args: 
                List with name, old and new phones.
            book:
                Address Book object.
        
        Returns:
            String with message.

        Raisese:
            TypeError: if no argument passed.
            ValueError: if current_number doesn't exist.
            PhoneValidationError: if phone number less then 10 digits.
        """
        name, current_number, new_number, *_ = args
        record = book.find(name)
        message = ''
        if record is not None:
            record.edit_phone(current_number, new_number)
            message = 'Contact updated'
        else:
            message = 'Contact is not found'
        return message

    @input_error_decorator()
    def show_phone(self, args: list, book: AddressBook) -> None:
        """Shows record with all its phones.
        
        Args:
            args:
                List with name.
            book:
                Address book object.
        
        Returns:
           None.

        Raises:
            ValueError: Not enough values to unpack.
        """
        name, *_ = args
        record = book.find(name)

        if record is not None:
            print(record)
        else:
            print('Contact is not found')

    def show_all(self, book: AddressBook) -> None:
        """Shows all records with phone numbers.
        
        Args:
            book:
                Address book object.

        Returns:
            None.
        """
        for record in book.data.values():
            print(record)

    @input_error_decorator()
    def add_birthday(self, args: list, book: AddressBook) -> str:
        """Adds birthday for contact.
        
        Args:
            args:
                List with name and birthday.
            book:
                Address book object.

        Returns:
            String with message.

        Raises:
             ValueError: Not enough values to unpack or date string is invalid.
        """
        name, birthday, *_ = args
        record = book.find(name)
        message = ''

        if record is not None:
            record.add_birthday(birthday)
            message = 'Birthday was added'
        else:
            message = 'Contact is not found'
        return message

    @input_error_decorator()
    def show_birthday(self, args: list, book: AddressBook) -> None:
        """Shows birthday for contact.
        
        Args:
            args:
                List with name.
            book:
                Address book object.
        
        Returns:
            None.
        """
        name, *_ = args
        record = book.find(name)

        if record is None:
            print('Contact is not found')
            return None

        if record.birthday is not None:
            print(record.birthday.value.strftime('%d.%m.%Y'))
        else:
            print('No birthday was added')

    def birthdays(self, book: AddressBook) -> None:
        """Shows all records with phone numbers.
        
        Args:
            book:
                Address book object.

        Returns:
            None.
        """
        upcomming_birthdays = book.get_upcoming_birthdays()
        for birthday in upcomming_birthdays:
            print(f"{birthday['name']} {birthday['congratulation_date']}")
