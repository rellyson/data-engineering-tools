#!/usr/bin/env python3

import sys

source_file = sys.argv[1]
dest_file = sys.argv[2]

with open(source_file, "r", encoding="utf-8") as input_file, open(
    dest_file, "w", encoding="utf-8"
) as output_file:
    lines = input_file.readlines()
    output_file.writelines(lines)

    input_file.close()
    output_file.close()
