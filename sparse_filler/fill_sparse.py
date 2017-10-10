#!/usr/bin/env python3


def line_list(line):
    """
    :param line: a string representing a line in the input file
    e.g. '2 3:1 7:1'
    :return: a list of elements
    e.g. ['2', '3:1', '7:1']
    """
    input_row_list = line.split()
    return input_row_list


def int_element_zero(line_list):
    """
    :param line_list: a list of strings, e.g. ['2', '3:1, '7:1']
    :return: an int from the first string element, e.g. 2
    """
    return int(line_list[0])


def int_before_colon(string_with_colon):
    """
    :param string_with_colon: a string with a colon e.g. '3:1'
    :return: an int e.g. 3
    """
    return int(string_with_colon.split(':')[0])


def filled(line):
    """
    :param line: a string representing a line in the input file
    e.g. ['1 3:1 7:1']
    :return: a list starting with 0,1,or 2 and then filled with 0 or 1
    e.g. [2, 0, 0, 1, 0, 0, 0, 1]
    """
    input_list = line_list(line)

    filled_list = list()

    filled_list.append(int_element_zero(input_list))

    row_list_tail = input_list[1:]
    element_int_previous = 0

    for string_with_colon in row_list_tail:

        element_int = int_before_colon(string_with_colon)

        number_of_zeroes = (element_int - element_int_previous) - 1
        for index in range(0, number_of_zeroes):
            filled_list.append(0)

        filled_list.append(1)

        # remember for next iteration
        element_int_previous = element_int

    return filled_list


def list_of_lists(input_filename):
    # https://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python#8010133

    nested_list = []

    with open(input_filename) as lines:
        for line in lines:
            filled_row = filled(line)
            nested_list.append(filled_row)

    return nested_list


input_filename = "../data/test_input0.txt"
vectors = list_of_lists(input_filename)
print('vectors', vectors)
