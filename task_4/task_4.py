import sys
from colorama import Fore, Style
from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error_add(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error_add
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def input_error_change(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and/or new number!"

    return inner

@input_error_change
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return "Contact changed."

# def input_error_change(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Enter name and/or new number!"

#     return inner

def print_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]

def print_contacts(contacts):
    if not contacts:
        return "The base is empty!"

    data_str = ""
    for key, value in contacts.items():
        data_str += f"Name: {key}, Phone: {value}\n"
    return data_str[0:-1]
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
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
                print(print_phone(args, contacts))
            case "all":
                print(print_contacts(contacts))
            case _:
                print("Invalid command.")
    
if __name__ == "__main__":
    main()