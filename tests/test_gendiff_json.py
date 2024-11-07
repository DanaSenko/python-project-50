import pytest
from gendiff import gendiff


def read_fixture(file_path):
    with open(file_path, "r") as file:
        return file.read()


def test_gendiff():
    with open("tests/fixtures/expected_diff.txt") as expected_file:
        expected_output = expected_file.read().strip()
    assert (
        gendiff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
        == expected_output
    )
