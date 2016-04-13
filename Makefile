MISSION = mission.sqm

MISSIONBUILDER = bin/missionbuilder.py

CLASSVEHICLE_SCRIPT = bin/$(@).py tmp/classMission/classVehicles.sqm | tee tmp/classMission/classVehicles.sqm2; mv tmp/classMission/classVehicles.sqm2 tmp/classMission/classVehicles.sqm

all: clean tmp classVehicles idpatcher lamps shops roadcones billboards cop_billboards Config $(MISSION)

CONFIG_VITEMS = ../Altis/Altis_Life.Altis/Config_vItems.hpp

Homepage:
	bin/homepage.py templates/homepage/index.html.skel | ssh root@xoreaxeax.de -t tee /var/www/html/index.html
	ssh root@xoreaxeax.de make -C /var/www/html

#
# generate the Configs from the macro expanders
#
Config:
	bin/vitems.py templates/Config/vItems.hpp | tee $(CONFIG_VITEMS)

#
# populate the working directory
#
tmp:
	mkdir -pv tmp
	rsync -Pavpx templates/mission/. tmp/.

#
# build the classVehicles class out of all Mapping projects and the original one from Altis Life
#
classVehicles:
	sed -i 's,\r,,g;' bin/slice.sh
	find ../Mapping -type f -ipath "*/mission*.sqm" | sort | uniq | \
		xargs -n1 --no-run-if-empty ./bin/slice.sh | \
			tee -a tmp/classMission/classVehicles.sqm

#
# chairs. CURRENTLY UNUSED. DO NOT ENABLE THIS!
#
#chairs:
#	$(CLASSVEHICLE_SCRIPT)
#

#
# all the cop billboards
#
cop_billboards:
	$(CLASSVEHICLE_SCRIPT)

#
# puts specific jpgs on top of these billboards that we know from xCam coordinates
#
billboards:
	$(CLASSVEHICLE_SCRIPT)

#
# turns on the lamps in xCam generated (CMF) mission.sqm files
#
lamps:
	$(CLASSVEHICLE_SCRIPT)

#
# add action handlers to shop laptops
#
shops:
	$(CLASSVEHICLE_SCRIPT)

#
# changes all the ids and item values in a file to consecutive numbers
#
idpatcher:
	$(CLASSVEHICLE_SCRIPT)

#
# sets allowDamage to true on all road cones in the mission file
#
roadcones:
	$(CLASSVEHICLE_SCRIPT)

#
# generate the mission now
#
$(MISSION):
	$(MISSIONBUILDER) tmp $(MISSION)

clean:
	rm -vrf tmp
	rm -vf $(MISSION)

