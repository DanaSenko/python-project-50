from gendiff.file_parser import parse_file
from gendiff.build_diff import build_diff
from formats.stylish import stylish
from formats.plain import plain


def gendiff(filepath1, filepath2, format_name="stylish"):
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    diff = build_diff(dict1, dict2)
    if format_name == "stylish":
        return stylish(diff)
    elif format_name == "plain":
        return plain(diff)
    raise ValueError
