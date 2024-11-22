import json
import yaml
import os


def parse_file(filepath):
    _, end_of_file = os.path.splitext(filepath)

    with open(filepath, "r") as file:
        match end_of_file:
            case ".json":
                return json.load(file)
            case ".yaml" | ".yml":
                return yaml.safe_load(file)
