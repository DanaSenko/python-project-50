from pathlib import Path
import pytest
from gendiff import generate_diff
from tests.fixtures.read_fixtures import read_expected_output


FIXTURES_DIR = Path(__file__).parent / "fixtures"

@pytest.mark.parametrize(
    "file1, file2, expected_output_file, format_name",
    [
        # Тесты для формата stylish
        (
            FIXTURES_DIR / "file1.json" ,
            FIXTURES_DIR / "file2.json",
            FIXTURES_DIR / "expected_stylish_output.txt",
            "stylish",
        ),
        (
            FIXTURES_DIR / "file1.yaml",
            FIXTURES_DIR / "file2.yaml",
            FIXTURES_DIR / "expected_stylish_output.txt",
            "stylish",
        ),
        # Тесты для формата plain
        (
            FIXTURES_DIR / "file1.json",
            FIXTURES_DIR / "file2.json",
            FIXTURES_DIR / "expected_plain_output.txt",
            "plain",
        ),
        (
            FIXTURES_DIR / "file1.yaml",
            FIXTURES_DIR / "file2.yaml",
            FIXTURES_DIR / "expected_plain_output.txt",
            "plain",
        ),
        # Тесты для формата json
        (
            FIXTURES_DIR / "file1.json",
            FIXTURES_DIR / "file2.json",
            FIXTURES_DIR / "expected_json_output.txt",
            "json",
        ),
        (
            FIXTURES_DIR / "file1.yaml",
            FIXTURES_DIR / "file2.yaml",
            FIXTURES_DIR / "expected_json_output.txt",
            "json",
        ),
    ],
)
def test_gendiff(file1, file2, expected_output_file, format_name):
    expected_output = read_expected_output(expected_output_file)
    assert generate_diff(
        file1, file2, format_name=format_name
    ) == expected_output
