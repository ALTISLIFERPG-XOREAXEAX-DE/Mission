#!/usr/bin/env python

import sys
import os

lamps = ["Land_LampHarbour_F", "Land_LampHalogen_F", "Land_LampAirport_F", "Land_LampDecor_F"]

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      lamp_found = 0

      if line.find("class Item") > 0:
        if line.find("this enableSimulation false;") > 0:
          for lamp in lamps:
            if line.find(lamp) > 0:
              if lamp_found == 0:
                output_buffer.append(line.replace("this enableSimulation false;", "this enableSimulation true;").replace("\r", "").replace("\n", ""))
                lamp_found = 1

      if lamp_found == 0:
        output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

