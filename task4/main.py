from typing import List, Tuple, Dict

def parse_input(user_input: str) -> Tuple[str, List]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(name: str, phone: str, contacts: Dict[str, str]) -> str:
    if contacts.get(name):
        return {}
    contacts[name] = phone
    return {name:phone}

def change_contact(name: str, phone: str, contacts: Dict[str, str]) -> str:
    contacts.update({name : phone})
    
def show_phone(name: str, contacts: Dict[str, str]) -> str:
    return contacts.get(name, 'Not Found')

def show_all(contacts: Dict[str, str]) -> None:
    return contacts.items()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if len(args) == 2:
            name = args[1]
        elif len(args) > 2:
            name, phone, _ = args
        else:
            print('Contact not added, wrong name and phone.')
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                contact = add_contact(name, phone, contacts)
                if not contact:
                    print("This name already exists, please enter different name.")
                else:
                    print("Contact added successfully.")
            case "phone":
                print(f'Contact and phone {name} : {show_phone(name)}')
            case "change":
                change_contact(name, phone, contacts)
                print("Contact updated successfully.")
            case "all":
                print('Contact and phone: ')
                if contacts:
                    for name, phone in show_all(contacts):
                        print(name, ':', phone)
                else:
                    print('No contacts.')
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()