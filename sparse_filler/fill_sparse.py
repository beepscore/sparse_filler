#!/usr/bin/env python3


def write_filled(input_filename):
    # https://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python#8010133

    with open(input_filename) as lines:
        for line in lines:
            print(line)


write_filled("../data/input.txt")
