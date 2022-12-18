import json


def task(input_filename: str, output_filename: str) -> None:
    ...  # TODO считать содержимое json файл input.json
    with open(input_filename, 'r') as json_input_file:
        content = json.load(json_input_file)

        with open(output_filename, 'w') as json_output_file:
            json.dump(content, json_output_file, indent=4)

    ...  # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
