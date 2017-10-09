#!/usr/bin/env python3


def filled(line):
    return line[:7]


def write_filled(input_filename, output_filename):
    # https://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python#8010133

    with open(output_filename, 'w') as output_file:

        with open(input_filename) as lines:
            for line in lines:
                result = filled(line)
                output_file.write(result)
                output_file.write('\n')


input_filename = "../data/input.txt"
output_filename = "../data/output.txt"
write_filled(input_filename, output_filename)