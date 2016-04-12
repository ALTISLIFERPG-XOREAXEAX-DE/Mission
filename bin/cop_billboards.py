#!/usr/bin/env python

import sys
import os

output_buffer = []

positions = []

positions.append("position[]={3347.881104,-1.13303,12972.75}")
positions.append("position[]={3360.217041,-1.13303,12964.266602}")
positions.append("position[]={3405.157471,-1.13303,12918.0908203}")
positions.append("position[]={3362.219971,-1.10273,12944.157227}")

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      if line.find("Land_Billboard_F") > 0:
        for position in positions:
          if line.find(position) > 0:
            line = line.replace("this setVectorUp", 'this setObjectTextureGlobal[0, ""textures\\billboards\\cops\\kavala\\noentry.jpg""]; this setVectorUp')

      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

