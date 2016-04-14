#!/usr/bin/env python

import sys
import os

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

this addAction[localize"STR_MAR_Clothing_Store",life_fnc_clothingMenu,"bruce"];

this addAction[localize"STR_MAR_General_Store",life_fnc_weaponShopMenu,"genstore"];

this addAction[localize"STR_Shops_Market",life_fnc_virt_menu,"market"];

this addAction[localize"STR_Shops_Cop",life_fnc_virt_menu,"cop"];

this addAction[localize"STR_Shops_Med",life_fnc_virt_menu,"med"];

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

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

dhs_shop_001 = """

this addAction[localize"STR_MAR_Rebel_Market",life_fnc_virt_menu,"rebel"];

this addAction[localize"STR_MAR_Rebel_Clothing_Shop",life_fnc_clothingMenu,"reb",0,false,false,"",' license_civ_rebel && playerSide == civilian'];

this addAction[localize"STR_MAR_Rebel_Weapon_Shop",life_fnc_weaponShopMenu,"rebel",0,false,false,"",' license_civ_rebel && playerSide == civilian'];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "rebel" >> "displayName")), [(getNumber(missionConfigFile >> "Licenses" >> "rebel" >> "price"))] call life_fnc_numberText],
	life_fnc_buyLicense,
	"rebel",
	0,
	false,
	false,
	"",
	' !license_civ_rebel && playerSide == civilian '
];

this addAction["<t color='#ADFF2F'>ATM</t>",life_fnc_atmMenu,"",0,FALSE,FALSE,"",' vehicle player == player && player distance _target < 4 '];

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

dhs_shop_002 = """

this addAction[localize"STR_MAR_Armament",life_fnc_weaponShopMenu,"gang",0,false,false,"",' license_civ_dhs && playerSide == civilian'];

this addAction[localize"STR_Shops_C_Gang",life_fnc_clothingMenu,"gang_clothing",0,false,false,"",' license_civ_rebel && playerSide == civilian'];

this setVariable["realname","Gang Armament"];

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

dhs_shop_003 = """

%s

""" % (shop_script)

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      line = line.replace('%%%DHS_SHOP_001%%%', dhs_shop_001.replace('"', '""'))
      line = line.replace('%%%DHS_SHOP_002%%%', dhs_shop_002.replace('"', '""'))
      line = line.replace('%%%DHS_SHOP_003%%%', dhs_shop_003.replace('"', '""'))

      output_buffer.append(line.replace("\r", " ").replace("\n", " ").replace("\t", " "))

  for line in output_buffer:
    print line

