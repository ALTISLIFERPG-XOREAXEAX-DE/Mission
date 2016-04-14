#!/usr/bin/env python

import sys
import os

boxes = [
"Box_East_Grenades_F",
"Box_East_Wps_F",
"Box_East_WpsLaunch_F",
"Box_East_WpsSpecial_F",
"Box_FIA_Ammo_F",
"Box_FIA_Support_F",
"Box_FIA_Wps_F",
"Box_NATO_Ammo_F",
"Box_NATO_AmmoOrd_F",
"Box_NATO_AmmoVeh_F",
"Box_NATO_Grenades_F",
"Box_NATO_Support_F",
"Box_NATO_Wps_F",
"Box_NATO_WpsLaunch_F",
"Box_NATO_WpsSpecial_F",
"CargoNet_01_box_F",
"Land_Ammobox_rounds_F",
"Land_CargoBox_V1_F",
"Land_Pallet_MilBoxes_F",
"Land_PaperBox_closed_F",
"Land_PaperBox_open_full_F",
"Land_WoodenBox_F",
"B_CargoNet_01_ammo_F"
]

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      if line.find("class Item") > 0:
        if line.find("this enableSimulation false;") > 0:
          for box in boxes:
            if line.find(box) > 0:
              line = line.replace("this enableSimulation false;", "this enableSimulation false; clearWeaponCargoGlobal this; clearMagazineCargoGlobal this; clearItemCargoGlobal this; this lock 2; ")

      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

