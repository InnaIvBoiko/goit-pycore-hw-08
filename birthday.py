from field import Field
from datetime import datetime
import re

class Birthday(Field):
    """Class for storing and validating birthday dates.
    
    Args:
        value (str): Date in DD.MM.YYYY format (e.g., "15.06.1990")
        
    Raises:
        ValueError: If date format is not DD.MM.YYYY or date is invalid
    """
    
    def __init__(self, value: str) -> None:
        try:
            # Validate exact format DD.MM.YYYY
            if not self._validate_format(value):
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
            # Convert string to datetime object
            birthday_date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    @staticmethod
    def _validate_format(date_str: str) -> bool:
        pattern = r'^(\d{2})\.(\d{2})\.(\d{4})$'
        return bool(re.match(pattern, date_str))