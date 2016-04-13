#!/usr/bin/env python

import sys
import os

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

