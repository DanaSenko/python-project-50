import json
import yaml
import os


def parse_file(filepath):
    _, end_of_file = os.path.splitext(filepath)

    with open(filepath, "r") as file:
        if end_of_file == ".json":
            return json.load(file)
        elif end_of_file in {".yaml", ".yml"}:
            return yaml.safe_load(file)
