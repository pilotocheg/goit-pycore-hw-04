def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Parses .txt file by given path string and returns lists of cats in the format `{ "id": <id>, "name": <name>, "age": <age> }`

    :param str path: a path to the .txt file containing cats in a format `<id>,<name>,<age>`
    """

    cats_info = []

    try:
        with open(path, mode="r", encoding="utf8") as file:
            for cat in file.readlines():
                id, name, age = cat.strip().split(",")
                cats_info.append({"id": id, "name": name, "age": age})

    except Exception as e:
        print(e)

    return cats_info
