def total_salary(path: str) -> tuple[int, int]:
    """
    Reads .txt file by given path string and calculates total and average salaries

    :param str path: a path to the .txt file containing workers in a format `<name>:<salary>`
    """

    total, average = 0, 0

    try:
        with open(path, mode="r", encoding="utf8") as file:
            workers = file.readlines()

            for worker in workers:
                _, salary = worker.strip().split(",")

                total += int(salary)

            average = total // len(workers)

    except Exception as e:
        print(e)

    return (total, average)
