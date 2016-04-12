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
      if line.find("Land_Billboard_F") > 0:
        #
        # Kavala Market Support Office
        #
        if line.find("position[]={3588.689453,8.22582,13151.123047}") > 0:
          line = line.replace("this setVectorUp [0,0,1]", 'this setVectorUp [0,0,1]; this setObjectTextureGlobal[0, ""textures\\billboards\\admin\\kavala\\support.jpg""]')

      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

