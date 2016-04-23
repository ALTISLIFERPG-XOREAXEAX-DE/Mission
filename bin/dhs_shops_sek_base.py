#!/usr/bin/env python

import sys
import os

output_buffer = []

shop_script = """

this addAction[
	"Heli Garage",
	{
		if(life_HC_isActive) then {
			[getPlayerUID player,playerSide,"Air",player] remoteExecCall ["HC_fnc_getVehicles",HC_Life];
		} else {
			[getPlayerUID player,playerSide,"Air",player] remoteExecCall ["TON_fnc_getVehicles",2];
		};

		life_garage_type = "Air";
		createDialog "Life_impound_menu";
		disableSerialization;
		ctrlSetText[2802,"Fetching Vehicles...."];
		life_garage_sp = "dhs_heli_spawn_001";
	}
];

this addAction[
	localize"STR_Garage_Title",
	{
		if(life_HC_isActive) then {
			[getPlayerUID player,playerSide,"Car",player] remoteExecCall ["HC_fnc_getVehicles",HC_Life];
		} else {
			[getPlayerUID player,playerSide,"Car",player] remoteExecCall ["TON_fnc_getVehicles",2];
		};
		
		life_garage_type = "Car";
		createDialog "Life_impound_menu";
		disableSerialization;
		ctrlSetText[2802,"Fetching Vehicles...."];
		life_garage_sp = "dhs_vehicle_spawn_001";
	}
];
		
this addAction[localize"STR_MAR_Store_vehicle_in_Garage",life_fnc_storeVehicle,"",0,false,false,"",'!life_garage_store'];

this addAction[
	localize "STR_MAR_Car_shop",
	life_fnc_vehicleShopMenu,
	["civ_car",civilian,"dhs_vehicle_spawn_001","civ","Bruce's New & Used Auto's"]
];

this addAction[
	localize"STR_MAR_Truck_Shop",
	life_fnc_vehicleShopMenu,
	["civ_truck",civilian,"dhs_vehicle_spawn_002","civ","Bruce's New & Used Trucks"]
];

this addAction[
	localize"STR_MAR_Helicopter_Shop",
	life_fnc_vehicleShopMenu,
	["civ_air",civilian,["dhs_heli_spawn_001","dhs_heli_spawn_002"],"civ","Carl's Airial Auto's"]
];

this addAction[
        "<t color='#ADFF2F'>ATM</t>",
        life_fnc_atmMenu,
        "",
        0,
        FALSE,
        FALSE,
        "",
        ' license_civ_dhs && playerSide == civilian && vehicle player == player && player distance _target < 4 '
];

this addAction[localize"STR_MAR_Clothing_Store",life_fnc_clothingMenu,"bruce"];

this addAction[localize"STR_MAR_General_Store",life_fnc_weaponShopMenu,"genstore"];

this addAction[localize"STR_Shops_W_Gun",life_fnc_weaponShopMenu,"gun",0,false,false,"",' license_civ_dhs && license_civ_gun && playerSide == civilian'];

this addAction[localize "STR_Shops_C_Gun",life_fnc_clothingMenu,"gun_clothing",0,false,false,"",' license_civ_dhs && license_civ_gun && playerSide == civilian'];

this addAction[
	format[
		"%1 ($%2)", localize (getText(missionConfigFile >> "Licenses" >> "gun" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "gun" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"gun",0,false,false,"",' license_civ_dhs && !license_civ_gun && playerSide == civilian '
];

this addAction[localize"STR_Shops_Market",life_fnc_virt_menu,"market"];

this addAction[localize"STR_Shops_Med",life_fnc_virt_menu,"med"];

this addAction[localize"STR_Shops_Pharmacy",life_fnc_virt_menu,"pharmacy"];

this addAction[
        format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "driver" >> "displayName")),
                [(getNumber(missionConfigFile >> "Licenses" >> "driver" >> "price"))] call life_fnc_numberText
        ],
        life_fnc_buyLicense,"driver",0,false,false,"",' license_civ_dhs && !license_civ_driver && playerSide == civilian '
];

this addAction[
        format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "boat" >> "displayName")),
                [(getNumber(missionConfigFile >> "Licenses" >> "boat" >> "price"))] call life_fnc_numberText
        ],
        life_fnc_buyLicense,"boat",0,false,false,"",' license_civ_dhs && !license_civ_boat && playerSide == civilian '
];

this addAction[
        format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "pilot" >> "displayName")),
                [(getNumber(missionConfigFile >> "Licenses" >> "pilot" >> "price"))] call life_fnc_numberText
        ],
        life_fnc_buyLicense,"pilot",0,false,false,"",' license_civ_dhs && !license_civ_pilot && playerSide == civilian '
];

this addAction[
        format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "trucking" >> "displayName")),
                [(getNumber(missionConfigFile >> "Licenses" >> "trucking" >> "price"))] call life_fnc_numberText
        ],
        life_fnc_buyLicense,"trucking",0,false,false,"",' license_civ_dhs && !license_civ_trucking && playerSide == civilian '
];

this addAction[
        format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "home" >> "displayName")),
                [(getNumber(missionConfigFile >> "Licenses" >> "home" >> "price"))] call life_fnc_numberText
        ],
        life_fnc_buyLicense,"home",0,false,false,"",' license_civ_dhs && !license_civ_home && playerSide == civilian '
];

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

dhs_shop_001 = """

this addAction[localize"STR_MAR_Rebel_Market",life_fnc_virt_menu,"rebel"];

this addAction[localize"STR_MAR_Rebel_Clothing_Shop",life_fnc_clothingMenu,"reb",0,false,false,"",' license_civ_dhs && playerSide == civilian && license_civ_rebel && playerSide == civilian'];

this addAction[localize"STR_MAR_Rebel_Weapon_Shop",life_fnc_weaponShopMenu,"rebel",0,false,false,"",' license_civ_dhs && playerSide == civilian && license_civ_rebel && playerSide == civilian'];

this addAction[
	localize"STR_MAR_W_E_Vehicle Shop",
	life_fnc_vehicleShopMenu,
	["reb_car",civilian,["dhs_vehicle_spawn_001","dhs_vehicle_spawn_002"],"reb","Rebel Motorpool - DHS Base"],
	0,
	false,
	false,
	"",
	' license_civ_dhs && playerSide == civilian && license_civ_rebel'
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "rebel" >> "displayName")), [(getNumber(missionConfigFile >> "Licenses" >> "rebel" >> "price"))] call life_fnc_numberText],
	life_fnc_buyLicense,
	"rebel",
	0,
	false,
	false,
	"",
	' license_civ_dhs && playerSide == civilian && !license_civ_rebel && playerSide == civilian '
];

this addAction["<t color='#ADFF2F'>ATM</t>",life_fnc_atmMenu,"",0,FALSE,FALSE,"",' license_civ_dhs && playerSide == civilian && vehicle player == player && player distance _target < 4 '];

this setObjectTextureGlobal[0, "textures\\armalife.jpg"]

"""

dhs_shop_002 = """

this addAction[localize"STR_Shops_Gang",life_fnc_virt_menu,"gang",0,false,false,"", ' license_civ_dhs && playerSide == civilian'];

this addAction[localize"STR_MAR_Armament",life_fnc_weaponShopMenu,"gang",0,false,false,"",' license_civ_dhs && playerSide == civilian'];

this addAction[localize"STR_Shops_C_Gang",life_fnc_clothingMenu,"gang_clothing",0,false,false,"",' license_civ_dhs && playerSide == civilian'];

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

