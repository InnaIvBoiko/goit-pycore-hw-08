from collections import UserDict
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from record import Record   
from constants import DATE_FORMAT, UPCOMING_DAYS

class AddressBook(UserDict[str, Record]):
    """Class for managing an address book.
    
    Inherits from UserDict to provide dictionary-like functionality
    while maintaining type safety and additional methods.
    """
    
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Contact {name} not found")
    
    def get_upcoming_birthdays(self, days: int = UPCOMING_DAYS) -> List[Dict[str, str]]:
        upcoming_birthdays = []
        today = datetime.now().date()
        
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date()
                birthday_this_year = birthday_date.replace(year=today.year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                days_until_birthday = (birthday_this_year - today).days
                
                if 0 <= days_until_birthday <= days:
                    congratulation_date = birthday_this_year
                    if congratulation_date.weekday() == 5:  # Saturday
                        congratulation_date += timedelta(days=2)  # Move to Monday
                    elif congratulation_date.weekday() == 6:  # Sunday
                        congratulation_date += timedelta(days=1)  # Move to Monday
                    
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
                    })
        
        return upcoming_birthdays
    
    def search_contacts(self, query: str) -> List[Record]:

        results = []
        query_lower = query.lower()
        
        for record in self.data.values():
            if query_lower in record.name.value.lower():
                results.append(record)
                continue
            
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
                    break
        
        return results
        
