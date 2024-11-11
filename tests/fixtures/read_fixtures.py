def read_expected_output(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
