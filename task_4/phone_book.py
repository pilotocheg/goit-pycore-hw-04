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
    return "\n".join([f"{name} {phone}" for name, phone in contacts.items()])
