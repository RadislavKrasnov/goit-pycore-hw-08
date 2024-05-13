"""Error handler"""

from typing import Callable, Any
from exceptions import PhoneValidationError

def input_error_decorator(
    value_error_message: str = '',
    key_error_message: str = '',
    index_error_message: str = 'Enter the argument for the command'
) -> Callable[[Callable], Callable]:
    """Returs input error handling function.
    
    Args:
        value_error_message:
            String with value error message.
        key_error_message:
            String with key error message.
        index_error_message:
            String with index error message.

    Returns:
        Callable function that handles input errors.
    """
    def input_error(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any|str:
            try:
                return func(*args, **kwargs)
            except ValueError as error:
                return value_error_message if value_error_message else error
            except KeyError as error:
                return key_error_message if key_error_message else error
            except IndexError as error:
                return index_error_message
            except PhoneValidationError as error:
                return error
        return inner
    return input_error
