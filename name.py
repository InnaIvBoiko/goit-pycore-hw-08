from field import Field
from datetime import datetime
from typing import Any

class Name(Field):
    """Class for storing contact names. Required field.
    
    Args:
        value (str): The contact's name
        
    Raises:
        ValueError: If name is empty or contains only whitespace
    """
    
    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value.strip())
        