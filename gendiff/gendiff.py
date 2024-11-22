from gendiff.file_parser import parse_file
from gendiff.build_diff import build_diff
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain
from gendiff.formats.json import json_format


def generate_diff(filepath1, filepath2, format_name="stylish"):
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    diff = build_diff(dict1, dict2)
    match format_name:
        case "stylish":
            return stylish(diff)
        case "plain":
            return plain(diff)
        case "json":
            return json_format(diff)
        case _:
            raise ValueError
