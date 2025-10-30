"""Utility functions for contact management bot application."""
from typing import List, Tuple
from decorators import input_error
from address_book import AddressBook
from record import Record
from record import Record

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Parse user input into command and arguments.
    
    Args:
        user_input (str): Raw user input string
        
    Returns:
        Tuple[str, List[str]]: Command and list of arguments
    """
    parts = user_input.split()
    if not parts:
        return "", []
    
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    """Add a new contact or add phone to existing contact.
    
    Args:
        args (List[str]): List containing name and phone number
        book (AddressBook): Address book instance
        
    Returns:
        str: Success message
        
    Raises:
        ValueError: If insufficient arguments provided
    """
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    """Change an existing contact's phone number.
    
    Args:
        args (List[str]): List containing name, old phone and new phone number
        book (AddressBook): Address book instance
        
    Returns:
        str: Success message
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    """Show a contact's phone numbers.
    
    Args:
        args (List[str]): List containing contact name
        book (AddressBook): Address book instance
        
    Returns:
        str: Contact's phone numbers
    """
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    if record.phones:
        return '; '.join(phone.value for phone in record.phones)
    else:
        return "No phone numbers found for this contact."


@input_error
def show_all(book: AddressBook) -> str:
    """Show all contacts in the address book.
    
    Args:
        book (AddressBook): Address book instance
        
    Returns:
        str: Formatted string of all contacts or message if no contacts found
    """
    if not book.data:
        return "No contacts found."
    result = ""
    for record in book.data.values():
        result += f"{record}\n"
    return result.strip()


@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    """Add birthday to an existing contact.
    
    Args:
        args (List[str]): List containing name and birthday
        book (AddressBook): Address book instance
        
    Returns:
        str: Success message
    """
    name, birthday = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    """Show a contact's birthday.
    
    Args:
        args: List containing contact name
        book: Address book instance
        
    Returns:
        str: Contact's birthday
    """
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    if record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")
    else:
        return "No birthday found for this contact."


@input_error
def birthdays(book: AddressBook) -> str:
    """Show upcoming birthdays in the next week.
    
    Args:
        book (AddressBook): Address book instance
        
    Returns:
        str: Formatted string of upcoming birthdays
    """
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    
    result = "Upcoming birthdays:\n"
    for birthday_info in upcoming:
        result += f"{birthday_info['name']}: {birthday_info['congratulation_date']}\n"
    return result.strip()


@input_error
def search_contacts(args: List[str], book: AddressBook) -> str:
    """Search for contacts by name or phone number.
    
    Args:
        args (List[str]): List containing search query
        book (AddressBook): Address book instance
        
    Returns:
        str: Formatted string of search results
    """
    if not args:
        raise ValueError("Enter search query")
    
    query = args[0]
    results = book.search_contacts(query)
    
    if not results:
        return f"No contacts found matching '{query}'"
    
    result = f"Found {len(results)} contact(s) matching '{query}':\n"
    for record in results:
        result += f"{record}\n"
    return result.strip()


@input_error
def remove_phone(args: List[str], book: AddressBook) -> str:
    """Remove a phone number from a contact.
    
    Args:
        args (List[str]): List containing name and phone number
        book (AddressBook): Address book instance
        
    Returns:
        str: Success message
    """
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    
    name, phone = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    
    record.remove_phone(phone)
    return f"Phone {phone} removed from {name}"