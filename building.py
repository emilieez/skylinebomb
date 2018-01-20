import pygame

from constants import *


class Building:
    coords = {}

    def __init__(self, left, height, right):
        self.left = left
        self.height = height
        self.right = right

        Building.coords[(left, right)] = height

    @classmethod
    def draw_buildings(cls, screen, data):
        for building in data:
            pygame.draw.rect(screen, BUILDING_COLOUR,
                             (building.left,
                              SCREEN_HEIGHT - building.height,
                              building.right - building.left,
                              building.height), 0)
