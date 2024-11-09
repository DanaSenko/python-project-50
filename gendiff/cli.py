#!/usr/bin/env python3

import argparse
from gendiff.gendiff import gendiff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    diff = gendiff(f"{args.first_file}", f"{args.second_file}", format_name="stylish")
    print(diff)
