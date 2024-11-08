import pytest
from gendiff import gendiff


def read_fixture(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "file1, file2, expected_output_file",
    [
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/expected_diff.txt",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/expected_diff.txt",
        ),
    ],
)
def test_gendiff(file1, file2, expected_output_file):
    expected_output = read_fixture(expected_output_file)
    assert gendiff(file1, file2) == expected_output
