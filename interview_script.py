"""Script for parsing a text document and finding some defined information"""


def open_file(file: str):
    """Open the text file and return its content as a list of lines."""
    try:
        with open(file, 'r', encoding="UTF-8") as fr:
            content = fr.readlines()
            line = []
            for _, content_line in enumerate(content):
                line.append(content_line.split())
        return line
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []


def parse_header(line: list) -> tuple:
    """Parse the header of the document to extract network element name and operation result."""
    element_name = line[0][1]
    operation_result = f"{line[3][3]} {line[3][4]}"
    return element_name, operation_result


def get_column_data(line: list, start: int, column_ind: int) -> list:
    """Extract data from a specific column ignoring first 9 lines"""
    column_data = []
    for i in line[start:]:
        if len(i) == 4:
            column_data.append(i[column_ind])
    return column_data


if __name__ == "__main__":
    TEXT_FILE = "network_element_data.txt"
    LINES = open_file(TEXT_FILE)

    network_element_name, result_of_the_operation = parse_header(LINES)
    print("Network Element Name:", network_element_name)
    print("Result of the Operation:", result_of_the_operation)

    START_LINE_INDEX = 9
    COLUMN1_INDEX = 1
    COLUMN2_INDEX = 2

    cell_name = get_column_data(LINES, START_LINE_INDEX, COLUMN1_INDEX)
    print("Data from column Cell Name:", cell_name)

    column_2 = get_column_data(LINES, START_LINE_INDEX, COLUMN2_INDEX)
    print("Data from column Column Name:", column_2)
