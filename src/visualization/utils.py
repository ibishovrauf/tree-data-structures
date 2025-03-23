def read_values_from_file(file_path: str) -> list:
    """
    Reads the file at file_path and returns a list of integers.
    Assumes that the file contains numbers separated by whitespace or newlines.
    """
    with open(f"data/{file_path}.txt", 'r') as file:
        content = file.read()
    # Split the content by whitespace and convert to integers
    numbers = [int(token) for token in content.split() if token.strip().isdigit()]
    return numbers
