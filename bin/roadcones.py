#!/usr/bin/env python

import sys
import os

cones = ["RoadCone_F"]

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      cone_found = 0

      if line.find("class Item") > 0:
        if line.find("this allowDamage false;") > 0:
          for cone in cones:
            if line.find(cone) > 0:
              if cone_found == 0:
                output_buffer.append(line.replace("this allowDamage false;", "this allowDamage true;").replace("\r", "").replace("\n", ""))
                cone_found = 1

      if cone_found == 0:
        output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

