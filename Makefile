MISSION = mission.sqm

MISSIONBUILDER = bin/missionbuilder.py

all: clean tmp classVehicles $(MISSION)

tmp:
	mkdir -pv tmp
	rsync -Pavpx templates/. tmp/.

classVehicles:
	sed -i 's,\r,,g;' bin/slice.sh
	find ../Mapping -type f -ipath "*/mission*.sqm" | sort | uniq | \
		xargs -n1 --no-run-if-empty ./bin/slice.sh | \
			tee -a tmp/classMission/.classVehicles.sqm1
	sed -i 's,\r,,g;' bin/lamps.sh
	bin/lamps.sh tmp/classMission/.classVehicles.sqm1 | tee tmp/classMission/.classVehicles.sqm2
	bin/idpatcher.py tmp/classMission/.classVehicles.sqm2 500 | tee tmp/classMission/classvehicles.sqm

$(MISSION):
	$(MISSIONBUILDER) tmp $(MISSION)

clean:
	rm -vrf tmp
	rm -vf $(MISSION)

