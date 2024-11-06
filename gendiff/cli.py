#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import gendiff

def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    diff = gendiff(f'data/{args.first_file}', f'data/{args.second_file}')
    print(diff)