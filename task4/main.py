from typing import List, Tuple, Dict

def parse_input(user_input: str) -> Tuple[str, List]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: Tuple[str, str], contacts: Dict[str, str]) -> str:
    try:
        name, phone = args
    except ValueError:
        return 'Contact not added, wrong name and phone.'
    if contacts.get(name):
        print("This name already exists, please enter different name.")
        return
    contacts[name] = phone
    return "Contact added successfully."

def change_contact(args: Tuple[str, str], contacts: Dict[str, str]) -> str:
    try:
        name, phone = args
    except ValueError:
        return 'Contact not added, wrong name and phone.'
    contacts.update({name : phone})
    return "Contact updated successfully."

def show_phone(args: Tuple[str, str], contacts: Dict[str, str]) -> str:
    return contacts.get(args[0], 'Not Found')

def show_all(contacts: Dict[str, str]) -> None:
    print('Contact and phone: ')
    if contacts:
        for name, phone in contacts.items():
            print(name, ':', phone)
    else:
        print('No contacts.')

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
            case "phone":
                print(f'Contact and phone {args[0]} : {show_phone(args, contacts)}')
            case "change":
                print(change_contact(args, contacts))
            case "all":
                show_all(contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()