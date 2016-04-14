#!/usr/bin/env python

import sys
import os

output_buffer = []

fuel_action = """

this setFuelCargo 0;

this addAction [
  localize "STR_Action_Pump",
  life_fnc_FuelStatOpen,
  1,
  3,
  true,
  true,
  "",
  ' _this distance _target < 5 && cursorTarget == _target '
]

"""

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      line = line.replace("%%%ACTION_FUEL_ACTION%%%", fuel_action)

      output_buffer.append(line.replace("\r", " ").replace("\n", " ").replace.("\t", " ")replace('"', '""'))

  for line in output_buffer:
    print line

