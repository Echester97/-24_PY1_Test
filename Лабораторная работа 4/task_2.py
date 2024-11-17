# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp:
        data_csv = csv.DictReader(inp, delimiter=",", lineterminator="\n")
        data = [row for row in data_csv]
    with open(OUTPUT_FILENAME,'w') as oup:
        json_data = json.dump(data,oup,indent=4)
    return json_data

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
