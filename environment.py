import math
import sys

from bomb import *
from building import *
from plane import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)

plane = Plane(screen, 100, 50, SCREEN_WIDTH // 2, 5)
bomb = Bomb(screen, BOMB_COLOUR, (0, 0), 10)


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


def set_text():
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render('SPACE...stop' + ' ' * 15 +
                                'LEFT/RIGHT...speed -/+' + ' ' * 15 +
                                'DOWN...bomb',
                                True, (255, 255, 255))
    screen.blit(textsurface, (100, 100))


def event_resolver(event):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYUP:
        plane.perform_key_events(event.key)
        if event.key == pygame.K_DOWN:
            bomb.x_pos = math.ceil(plane.x_pos + plane.width / 2)
            bomb.y_pos = math.ceil(plane.y_pos + plane.height)
            Bomb.drop = True
