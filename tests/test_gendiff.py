import pytest
from gendiff import generate_diff
from tests.fixtures.read_fixtures import read_expected_output


@pytest.mark.parametrize(
    "file1, file2, expected_output_file, format_name",
    [
        # Тесты для формата stylish
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/expected_stylish_output.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/expected_stylish_output.txt",
            "stylish",
        ),
        # Тесты для формата plain
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/expected_plain_output.txt",
            "plain",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/expected_plain_output.txt",
            "plain",
        ),
        # Тесты для формата json
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/expected_json_output.txt",
            "json",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/expected_json_output.txt",
            "json",
        ),
    ],
)
def test_gendiff(file1, file2, expected_output_file, format_name):
    expected_output = read_expected_output(expected_output_file)
    assert generate_diff(file1, file2, format_name=format_name) == expected_output
