MISSION = mission.sqm

MISSIONBUILDER = bin/missionbuilder.py

all: clean tmp classVehicles idpatcher lamps $(MISSION)

#
# populate the working directory
#
tmp:
	mkdir -pv tmp
	rsync -Pavpx templates/. tmp/.

#
# build the classVehicles class out of all Mapping projects and the original one from Altis Life
#
classVehicles:
	sed -i 's,\r,,g;' bin/slice.sh
	find ../Mapping -type f -ipath "*/mission*.sqm" | sort | uniq | \
		xargs -n1 --no-run-if-empty ./bin/slice.sh | \
			tee -a tmp/classMission/classVehicles.sqm

#
# turns on the lamps in xCam generated (CMF) mission.sqm files
#
lamps:
	bin/lamps.py tmp/classMission/classVehicles.sqm | tee tmp/classMission/classVehicles.sqm2
	mv tmp/classMission/classVehicles.sqm2 tmp/classMission/classVehicles.sqm

#
# changes all the ids and item values in a file to consecutive numbers
#
idpatcher:
	bin/idpatcher.py tmp/classMission/classVehicles.sqm 500 | tee tmp/classMission/classvehicles.sqm2
	mv tmp/classMission/classVehicles.sqm2 tmp/classMission/classVehicles.sqm

$(MISSION):
	$(MISSIONBUILDER) tmp $(MISSION)

clean:
	rm -vrf tmp
	rm -vf $(MISSION)

