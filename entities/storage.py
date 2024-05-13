"""Address book storage module"""

import pickle
from .address_book import AddressBook

class Storage:
    """Stores address book contacts in file"""

    def save_data(self, book: AddressBook, filename: str ="addressbook.pkl") -> None:
        """Saves address book into file.
        
        Args:
            book:
                Address book object.
            filename:
                String with name of file where address book data will be stored.

        Returns:
            None.
        """
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(self, filename: str ="addressbook.pkl") -> AddressBook:
        """Loads data from file.
        
        Args:
            filename:
                String with name of file where address book data is stored.

        Returns:
            Address book object.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()
