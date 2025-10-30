from typing import List, Any, Tuple
from address_book import AddressBook
from constants import DATE_FORMAT, UPCOMING_DAYS


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Parse user input into command and arguments."""
    parts = user_input.split()
    if not parts:
        return "", []
    
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args
    
    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            from utils import add_contact
            print(add_contact(args, book))

        elif command == "change":
            from utils import change_contact
            print(change_contact(args, book))

        elif command == "phone":
            from utils import show_phone
            print(show_phone(args, book))

        elif command == "all":
            from utils import show_all
            print(show_all(book))

        elif command == "add-birthday":
            from utils import add_birthday
            print(add_birthday(args, book))

        elif command == "show-birthday":
            from utils import show_birthday
            print(show_birthday(args, book))

        elif command == "birthdays":
            from utils import birthdays
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()    