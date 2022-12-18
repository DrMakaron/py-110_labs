INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, 'r') as input_file:
        data = input_file.readlines()
        with open(OUTPUT_FILE, 'w') as output_file:
            output_file.writelines(map(str.upper, data))


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
