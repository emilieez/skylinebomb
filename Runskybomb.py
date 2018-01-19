import sys

import pygame

from building import *
from constants import *
from plane import Plane
from skyproblem import get_sky_line


def get_skydata():
    skydata = str(get_sky_line()).split()

    buildings = []
    idx = 0
    while idx < len(skydata) - 2:
        buildings.append(Building(int(skydata[idx]) * 22, int(skydata[idx + 1]) * 22, int(skydata[idx + 2]) * 22))
        idx += 2

    return buildings


def draw_buildings():
    pass


if __name__ == '__main__':
    draw_buildings()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Blocker")

    for building in get_skydata():
        pygame.draw.rect(screen, BLUE,
                         (building.left,
                          SCREEN_HEIGHT - building.height,
                          building.right - building.left,
                          building.height
                          ), 0)

    block_size = 100, 100, 100, 100
    plane = Plane(screen, 50, 50, SCREEN_WIDTH // 2, 0, )

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        plane.move(0.5)
        pygame.display.update()