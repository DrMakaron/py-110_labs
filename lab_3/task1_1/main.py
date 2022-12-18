INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE, 'r') as file:  # TODO открыть указатель на файл
        data = file.readlines()

        for line in data:# TODO файл является итератором, который работает с циклом for в построчном режиме
            print(line.rstrip())


if __name__ == "__main__":
    task()
