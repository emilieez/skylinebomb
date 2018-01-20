import math
import sys

from bomb import *
from building import *
from plane import *


def get_skydata():
    input_file = open(SKYDATA)

    buildings = []
    for line in input_file:
        coords = line.split()
        buildings.append(Building(int(coords[0]) * 22, int(coords[1]) * 22, int(coords[2]) * 22))

    return buildings


def get_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    return screen


def draw_buildings(screen):
    for building in get_skydata():
        pygame.draw.rect(screen, BUILDING_COLOUR,
                         (building.left,
                          SCREEN_HEIGHT - building.height,
                          building.right - building.left,
                          building.height), 0)


def get_plane(screen):
    return Plane(screen, 100, 50, SCREEN_WIDTH // 2, 5)


def get_bomb(screen):
    return Bomb(screen, BOMB_COLOUR, (0, 0), 10)


def event_resolver(event, plane, bomb):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYUP:
        plane.perform_key_events(event.key)
        if event.key == pygame.K_DOWN:
            bomb.x_pos = math.ceil(plane.x_pos + plane.width / 2)
            bomb.y_pos = math.ceil(plane.y_pos + plane.height)
            Bomb.drop = True
