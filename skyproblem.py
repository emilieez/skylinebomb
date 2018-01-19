from building import Building
from skyline import Skyline

INPUTFILE = "skydata.txt"


def get_sky_line():
    input_file = open(INPUTFILE)

    buildings = []
    for line in input_file:
        coords = line.split()
        building = Building(int(coords[0]), int(coords[1]), int(coords[2]))
        buildings.append(building)

    the_skyline = Skyline()
    for building in buildings:
        the_skyline.add(building)

    return the_skyline