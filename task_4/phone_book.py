contacts = {}


def add_contact(name: str, phone: str):
    contacts[name] = phone
    return "Contact added."


def change_contact(name: str, phone: str):
    contacts[name] = phone
    return "Contact changed."


def show_phone(name: str):
    return contacts[name]


def show_all():
    contacts_items = contacts.items()
    contacts_count = len(contacts_items)
    contacts_str = ""
    for index, (name, phone) in enumerate(contacts_items):
        contacts_str += f"{name} {phone}"
        if index < (contacts_count - 1):
            contacts_str += "\n"

    return contacts_str
