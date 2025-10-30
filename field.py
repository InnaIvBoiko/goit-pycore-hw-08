from typing import Any

class Field:
    """Basic class for record fields."""
    
    def __init__(self, value: Any) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)