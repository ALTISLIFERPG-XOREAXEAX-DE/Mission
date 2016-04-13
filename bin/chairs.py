#!/usr/bin/env python

import sys
import os

chairs = ["Land_ChairWood_F", "Land_ChairPlastic_F", "Land_OfficeChair_01_F", "Land_CampingChair_V1_F"]

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:

      if line.find("class Item") > 0:
        if line.find("this allowDamage false;") > 0:
          for chair in chairs:
            if line.find(chair) > 0:
              line = line.replace("this allowDamage false;", 'this allowDamage false; this addAction [""sit down"", ""custom\scripts\sitdown.sqf""];')

      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

