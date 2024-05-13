"""Entry point of the application."""

from entities import InputParser
from entities import CommandHandler
from entities import Storage

class Bootstrap:
    """Bootstrap the application."""

    def run(self):
        """Runs the address book bot."""
        storage = Storage()
        book = storage.load_data()
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            input_parser = InputParser()
            command_handler = CommandHandler()
            command, *args = input_parser.parse_input(user_input)

            if command in ["close", "exit"]:
                storage.save_data(book)
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(command_handler.add_contact(args, book))
            elif command == "change":
                print(command_handler.change_contact(args, book))
            elif command == "phone":
                command_handler.show_phone(args, book)
            elif command == "all":
                command_handler.show_all(book)
            elif command == "add-birthday":
                print(command_handler.add_birthday(args, book))
            elif command == "show-birthday":
                command_handler.show_birthday(args, book)
            elif command == "birthdays":
                command_handler.birthdays(book)
            else:
                print("Invalid command.")

if __name__ == "__main__":
    bootstrap = Bootstrap()
    bootstrap.run()
