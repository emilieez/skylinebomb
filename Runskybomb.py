import math
import sys

from bomb import *
from building import *
from constants import *
from plane import Plane


def get_skydata():
    input_file = open(SKYDATA)

    buildings = []
    for line in input_file:
        coords = line.split()
        buildings.append(Building(int(coords[0]) * 22, int(coords[1]) * 22, int(coords[2]) * 22))

    return buildings


def draw_buildings():
    for building in get_skydata():
        pygame.draw.rect(screen, BUILDING_COLOUR,
                         (building.left,
                          SCREEN_HEIGHT - building.height,
                          building.right - building.left,
                          building.height), 0)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Blocker")

    draw_buildings()

    block_size = 100, 100, 100, 100
    plane = Plane(screen, 100, 50, SCREEN_WIDTH // 2, 0, )
    bomb = Bomb(screen, GREEN, (plane.x_pos, plane.y_pos), 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                plane.perform_key_events(event.key)
                if event.key == pygame.K_DOWN:
                    bomb.x_pos = math.ceil(plane.x_pos)
                    bomb.y_pos = math.ceil(plane.y_pos)
                    Bomb.drop = True

        plane.move()
        bomb.drop_bomb()
        pygame.display.update()