import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла

    with open(filename, 'r') as json_file:
        content = json.load(json_file)

    return max(content, key=lambda item: item["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
