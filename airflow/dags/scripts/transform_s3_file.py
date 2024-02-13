#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as source_file, open(
    output_file, "w", encoding="utf-8"
) as dest_file:
    lines = source_file.readlines()
    dest_file.writelines(lines)
