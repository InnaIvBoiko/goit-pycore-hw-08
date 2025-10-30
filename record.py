from typing import List, Optional
from constants import DATE_FORMAT
from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    """Class for storing contact information, including name and list of phones.
    
    Args:
        name (str): Contact's name
        
    Attributes:
        name (Name): Contact's name object
        phones (List[Phone]): List of phone numbers
        birthday (Optional[Birthday]): Contact's birthday
    """

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: str) -> None:
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
    
    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)
    
    def remove_phone(self, phone: str) -> None:
        phone_to_remove = None
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                phone_to_remove = phone_obj
                break
        
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone {phone} not found")
    
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_found = False
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:

                if not Phone.validate_phone(new_phone):
                    raise ValueError("New phone number must contain exactly 10 digits")
                phone_obj.value = new_phone
                phone_found = True
                break
        
        if not phone_found:
            raise ValueError(f"Phone {old_phone} not found")
    
    def find_phone(self, phone: str) -> Optional[Phone]:
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self) -> str:
        phones_str = '; '.join(phone_obj.value for phone_obj in self.phones)
        birthday_str = f", birthday: {self.birthday.value.strftime(DATE_FORMAT)}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

