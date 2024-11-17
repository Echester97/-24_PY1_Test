# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as f:
        input_data = json.load(f)
    data_list = [item['score']*item['weight'] for item in input_data]
    return round(sum(data_list), 3)


print(task())
