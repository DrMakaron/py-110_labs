OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO записать лесенку в файл
    with open(OUTPUT_FILE, 'w') as txt_file:
        for step in range(1, 11):
            txt_file.write(f"{step * '*':>10}\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
