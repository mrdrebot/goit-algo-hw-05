from functools import wraps
from typing import Callable

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd: str = cmd.strip().lower()
    return cmd, *args

def input_error_add(func: Callable[[tuple], Callable[[tuple], tuple]]) -> Callable[[tuple], Callable[[tuple], tuple]]:
    @wraps(func)
    def inner(*args: tuple) ->  Callable[[tuple], Callable[[tuple], tuple]]:
        try:
            if len(args[0]) < 2:
                raise IndexError("You need to provide both name and phone!")

            name, phone = args[0]

            if name.isdigit() or not phone.isdigit():
                raise ValueError("Name must contain symbols and phone number only digits!")

            if name in args[1]:
                raise KeyError("Entered name is already exist. Change name or use another command to change phone number!")

            return func(*args)
        except ValueError as e:
            return f"Error: { e }"
        except KeyError as e:
            return f"Error: { e }"
        except IndexError as e:
            return f"Error: { e }"

    return inner

@input_error_add
def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def input_error_change(func: Callable[[tuple], Callable[[tuple], tuple]]) -> Callable[[tuple], Callable[[tuple], tuple]]:
    @wraps(func)
    def inner(*args: tuple) ->  Callable[[tuple], Callable[[tuple], tuple]]:
        try:
            if len(args[0]) < 2:
                raise IndexError("You need to provide both name and phone!")

            name, phone = args[0]

            if name.isdigit() or not phone.isdigit():
                raise ValueError("Name must contain symbols and phone number only digits!")

            if name not in args[1]:
                raise KeyError("Entered name hasn't find in base!")

            return func(*args)
        except ValueError as e:
            return f"Error: { e }"
        except KeyError as e:
            return f"Error: { e }"
        except IndexError as e:
            return f"Error: { e }"

    return inner

@input_error_change
def change_contact(args: list, contacts: dict):
    name, phone = args

    if name in contacts:
        contacts[name] = phone

    return "Contact changed."

def input_error_show_phone(func: Callable[[tuple], Callable[[tuple], tuple]]) -> Callable[[tuple], Callable[[tuple], tuple]]:
    @wraps(func)
    def inner(*args: tuple) ->  Callable[[tuple], Callable[[tuple], tuple]]:
        try:
            if len(args[0]) < 1:
                raise IndexError("You need to provide name!")

            name = args[0][0]

            if name.isdigit():
                raise ValueError("Entered name contain only digits!")

            if name not in args[1]:
                raise KeyError("Entered name hasn't find in base!")

            return func(*args)
        except ValueError as e:
            return f"Error: { e }"
        except KeyError as e:
            return f"Error: { e }"
        except IndexError as e:
            return f"Error: { e }"

    return inner

@input_error_show_phone
def show_phone(args: list, contacts: dict):
    name = args[0]

    if name in contacts:
        return contacts[name]

def input_error_show_all(func: Callable[[tuple], Callable[[tuple], tuple]]) -> Callable[[tuple], Callable[[tuple], tuple]]:
    @wraps(func)
    def inner(*args: tuple) ->  Callable[[tuple], Callable[[tuple], tuple]]:
        try:
            if not args[0]:
                raise ValueError("The base is empty!")
            
            return func(*args)
        except ValueError as e:
            return f"Error: { e }"

    return inner

@input_error_show_all
def show_all(contacts: dict):
    data_str: str = ""
    for key, value in contacts.items():
        data_str += f"Name: {key}, Phone: {value}\n"

    return data_str[0:-1]
    
def main():
    contacts: dict = {}
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input: str = input("Enter a command: ")
            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(show_phone(args, contacts))
                case "all":
                    print(show_all(contacts))
                case _:
                    print("Invalid command. You can use this command: add, change, phone, all, close or exit!")
        except ValueError:
            print("Please, enter a command!")

if __name__ == "__main__":
    main()