"""Script for parsing a text document and finding some defined information"""


def open_file(txt_file: str):
    """This function will open the text file and returning the content as lines"""

    with open(txt_file, 'r') as fr:
        content = fr.readlines()
        line = []
        for i, content_line in enumerate(content):
            line.append(content_line.split())

    return line
def get_content(line: list) -> tuple:
    """This function will get the Title of the device and the Status of operation """

    network_element_name = line[0][1]
    result_of_the_operation = line[3][3] + " " + line[3][4]

    return network_element_name, result_of_the_operation

def get_column_data(lines:list, start_line_ind: int, column_ind: int) -> str:
    """This function will get the data from the column of interest"""
    column_data = []

    for line in lines[start_line_ind:]:
        if len(line) == 4:
            column_data.append(line[column_ind])

    return column_data

if __name__ == "__main__":
    txt_file = "network_element_data.txt"
    lines = open_file(txt_file)
    network_element_name, result_of_the_operation = get_content(lines)
    # print(lines)
    print("Network Element Name:", network_element_name)
    print("Result of the Operation:", result_of_the_operation)
    start_line_ind = 9
    column_ind_1 = 1
    column_ind_2 = 2
    cell_name = get_column_data(lines, start_line_ind, column_ind_1)
    # print("Data from column Cell Name :", cell_name)
    column_2 = get_column_data(lines, start_line_ind, column_ind_2)
    # print("Data from column Column Name :", column_2)

