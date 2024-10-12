import phone_book
import re


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def parse_value_error(e: ValueError):
    result = re.search(r"not enough values to unpack \(expected (\d)", str(e))

    if result:
        missing_args = int(result.group(1))
        return f"Should be {missing_args} argument{"s" if missing_args > 1 else ""} after the command"

    return "Invalid command."


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        try:
            match command:
                case "hello":
                    print("How can I help you?")

                case "add":
                    name, phone = args
                    print(phone_book.add_contact(name, phone))

                case "change":
                    name, phone = args
                    print(phone_book.change_contact(name, phone))

                case "phone":
                    (name,) = args
                    print(phone_book.show_phone(name))

                case "all":
                    print(phone_book.show_all())

                case _:
                    print("Invalid command.")
        except ValueError as e:
            print(parse_value_error(e))


if __name__ == "__main__":
    main()
