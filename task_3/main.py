import sys
from logger import log_dir_tree

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(
            "Please, provide the path to the dir as the second argument in the console"
        )
    else:
        log_dir_tree(sys.argv[1])
