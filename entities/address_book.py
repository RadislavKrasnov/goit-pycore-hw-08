"""Address book entity."""

from collections import UserDict
from datetime import datetime, timedelta
from .record import Record

class AddressBook(UserDict):
    """Represents address book with contact records.
    
    Attributes:
        data:
          Dictionary with contact records.  
    """

    def add_record(self, record: Record) -> None:
        """Adds record into address book.
        
        Args:
            record:
                Record type object with name and the list of phones.
        
        Returns:
            None.
        
        Raises:
            TypeError: if argument isn't passed.
            AttributeError: if argument doesn't have name attribute.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record|None:
        """Finds record object from the address book by name.
        
        Args:
            name:
                String with name of the contact by which record must be found.
        
        Returns:
             Record type object with name and the list of phones.
             None type if any record isn't found by the given name.
        
        Raises:
            TypeError: if missing 1 required positional argument.
        """
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        """Deletes record from address book by name
        
        Args:
            name:
                String with name of the contact by which record must be found.
        
        Returns:
            None.
        
        Raises:
            KeyError: if incorrect argument type or value is passed.
            TypeError: if argument is missed.
        """
        del self.data[name]

    def get_upcoming_birthdays(self) -> list:
        """Returns list of users that have birthday withing 7 days including current date
        
        Returns:
            List of birthdays.
        """
        today = datetime.today().date()
        current_year =datetime.now().year
        end_of_week_date = today + timedelta(days=7)
        upcoming_birthdays = []

        try:
            for record in self.data.values():
                birth_date = record.birthday

                if birth_date is None:
                    continue

                birth_date = birth_date.value.strftime('%d.%m.%Y')
                birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
                birthday_this_year = birth_date.replace(year=current_year)

                if birthday_this_year < today:
                    birth_date = birth_date.replace(year=current_year + 1)
                else:
                    birth_date = birthday_this_year

                if today <= birth_date <= end_of_week_date:
                    if birth_date.weekday() > 4:
                        days_delta = 7 - birth_date.weekday()
                        birth_date += timedelta(days=days_delta)

                    upcoming_birthdays.append({
                        'name': record.name.value, 
                        'congratulation_date': birth_date.strftime('%d.%m.%Y')
                    })
        except TypeError as e:
            print(e) # logger
        return upcoming_birthdays
