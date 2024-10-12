from colorama import Fore
from pathlib import Path
from .exceptions import NotADir, NotExists


def log(name: str, color: str, level: int):
    print(f"{'  ' * level}{color}{name}")


def log_file(path: Path, level: int, is_last=False):
    log(f"📜{path.name}", color=Fore.GREEN, level=level)


def log_dir(path: Path, level=0, is_last=False):
    log(f"📂{path.name}/", color=Fore.BLUE, level=level)

    for child_path in path.iterdir():

        if child_path.is_dir():
            log_dir(child_path, level=level + 1)
        else:
            log_file(child_path, level=level + 1)


def log_dir_tree(path_str: str):
    try:
        path = Path(path_str)

        if not path.exists():
            raise NotExists(f"Provided path {path_str} not exists")
        if not path.is_dir():
            raise NotADir(f"Provided path {path_str} is not a dir")

        log_dir(path)

    except Exception as e:
        print("An exception occurred:", e)
