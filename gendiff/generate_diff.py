from gendiff.file_parser import read_json_file
from formats.json_format import to_json


def generate_diff(dict1, dict2):
    keys = sorted(set(dict1.keys() | dict2.keys()))
    result = ["{"]

    for key in keys:
        value1 = to_json(dict1.get(key))
        value2 = to_json(dict2.get(key))

        if key in dict1 and key not in dict2:
            result.append(f"  - {key}: {value1}")
        elif key in dict2 and key not in dict1:
            result.append(f"  + {key}: {value2}")
        elif dict1[key] != dict2[key]:
            result.append(f"  - {key}: {value1}")
            result.append(f"  + {key}: {value2}")
        else:
            result.append(f"    {key}: {value1}")
    result.append("}")

    return "\n".join(result)


def gendiff(filepath1, filepath2):
    dict1 = read_json_file(filepath1)
    dict2 = read_json_file(filepath2)
    diff = generate_diff(dict1, dict2)

    return diff
