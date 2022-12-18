import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    gen_exr = (item["contains_improvement_appeals"] for item in data)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
