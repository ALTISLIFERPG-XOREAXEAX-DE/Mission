#!/usr/bin/env python

import sys
import os

shops = ["Land_Laptop_device_F"]

output_buffer = []

shop_script = """

this addAction[
	"<t color='#ADFF2F'>ATM</t>",
	life_fnc_atmMenu,
	"",
	0,
	FALSE,
	FALSE,
	"",
	' vehicle player == player && player distance _target < 4 '
];

this addAction[localize"STR_Shops_Market",life_fnc_virt_menu,"market"];
this addAction[localize"STR_MAR_General_Store",life_fnc_weaponShopMenu,"genstore"];
this addAction[localize"STR_MAR_Clothing_Store",life_fnc_clothingMenu,"bruce"];

this addAction[localize"STR_Shops_Cop",life_fnc_virt_menu,"cop"];
this addAction[localize"STR_Shops_Med",life_fnc_virt_menu,"med"];
this addAction[localize"STR_Shops_Admin",life_fnc_virt_menu,"admin"];

this addAction[localize"STR_MAR_EMS_Item_Shop",life_fnc_weaponShopMenu,"med_basic"];
this addAction[localize"STR_MAR_EMS_Clothing_Shop",life_fnc_clothingMenu,"med_clothing"];

this addAction[localize"STR_Shops_Pharmacy",life_fnc_virt_menu,"pharmacy"];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "driver" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "driver" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"driver",0,false,false,"",' !license_civ_driver && playerSide == civilian '
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "boat" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "boat" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"boat",0,false,false,"",' !license_civ_boat && playerSide == civilian '
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "pilot" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "pilot" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"pilot",0,false,false,"",' !license_civ_pilot && playerSide == civilian '
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "trucking" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "trucking" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"trucking",0,false,false,"",' !license_civ_trucking && playerSide == civilian '
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "home" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "home" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"home",0,false,false,"",' !license_civ_home && playerSide == civilian '
];

this setFuelCargo 0;
this addAction [localize "STR_Action_Pump",life_fnc_FuelStatOpen,1,3,true,true,"",' _this distance _target < 5 && cursorTarget == _target '];

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      shop_found = 0

      if line.find("class Item") > 0:
        if line.find("this enableSimulation false;") > 0:
          for shop in shops:
            if line.find(shop) > 0:
              if shop_found == 0:
                output_buffer.append(line.replace("this enableSimulation false;", "this enableSimulation false; %s; " % shop_script.replace('"', '""')).replace("\r", " ").replace("\n", " ").replace("\t", " "))
                shop_found = 1

      if shop_found == 0:
        output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

