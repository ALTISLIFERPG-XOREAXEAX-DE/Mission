MISSION = mission.sqm

MISSIONBUILDER = bin/missionbuilder.py

all: $(MISSION)

$(MISSION):
	$(MISSIONBUILDER) templates $(MISSION)

clean:
	rm -vf $(MISSION)

