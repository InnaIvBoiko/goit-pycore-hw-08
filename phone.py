from field import Field

class Phone(Field):
    """Class for storing and validating phone numbers.
    
    Args:
        value (str): Phone number in any format (must contain exactly 10 digits)
        
    Raises:
        ValueError: If phone number doesn't contain exactly 10 digits
    """
    
    def __init__(self, value: str) -> None:
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        digits_only = ''.join(filter(str.isdigit, phone))
        return len(digits_only) == 10