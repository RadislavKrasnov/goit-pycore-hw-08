"""Field entity."""

from dataclasses import dataclass

@dataclass
class Field:
    """Represents field in the address book's record.
    
    Attributes:
        value:
            String with field's value.
    """
    value: str

    def __str__(self) -> str:
        """Returns human readable information of the object.
        
        Returns:
            String with information about object.
        """
        return str(self.value)
