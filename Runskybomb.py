import math
import sys

from bomb import *
from building import *
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
    plane = Plane(screen, 50, 50, SCREEN_WIDTH // 2, 0, )
    bomb = Bomb(screen, (0, 255, 0), (plane.x_pos, plane.y_pos), 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                plane.perform_key_events(event.key)
                if event.key == pygame.K_DOWN:
                    bomb.x_pos = math.floor(plane.x_pos)
                    bomb.y_pos = math.floor(plane.y_pos)
                    Bomb.drop = True

        plane.move()
        bomb.drop_bomb()
        pygame.display.update()
