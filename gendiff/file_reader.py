import json


def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)