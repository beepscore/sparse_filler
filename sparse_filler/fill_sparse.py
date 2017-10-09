#!/usr/bin/env python3


def filled(line):
    """
    :param line: a string representing a line in the input file
    :return: a list starting with 0,1,or 2 and then filled with 0 or 1
    """
    return [0, 0, 1]


def write_filled(input_filename, output_filename):
    # https://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python#8010133

    with open(output_filename, 'w') as output_file:

        with open(input_filename) as lines:
            for line in lines:
                filled_list = filled(line)
                filled_string = " ".join(str(x) for x in filled_list)
                output_file.write(filled_string)
                output_file.write('\n')


input_filename = "../data/input.txt"
output_filename = "../data/output.txt"
write_filled(input_filename, output_filename)
